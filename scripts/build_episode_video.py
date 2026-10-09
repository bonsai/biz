#!/usr/bin/env python3
"""Build VOICEVOX narration and an MP4 for one episode."""
import json, os, re, subprocess, wave
from pathlib import Path
import requests
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/"dist"
EPISODE=int(os.getenv("EPISODE","1"))
SPEAKER=int(os.getenv("VOICEVOX_SPEAKER","3"))
API=os.getenv("VOICEVOX_URL","http://127.0.0.1:50021").rstrip("/")
def main():
    if not 1 <= EPISODE <= 31: raise ValueError("EPISODE must be between 1 and 31")
    meta=next(json.loads(x) for x in (ROOT/"episodes.jsonl").read_text(encoding="utf-8").splitlines() if x.strip() and int(json.loads(x)["episode"])==EPISODE)
    manuscript=ROOT/meta["path"]
    if not manuscript.is_file(): raise FileNotFoundError(manuscript)
    image=next((p for p in [ROOT/"assets/images"/f"{EPISODE:02d}.png",ROOT/"assets/images"/f"{EPISODE}.png"] if p.is_file()),None)
    if image is None: raise FileNotFoundError(f"Add Gemini image: assets/images/{EPISODE:02d}.png")
    text=manuscript.read_text(encoding="utf-8")
    text=re.sub(r"^---\s*$.*?^---\s*$","",text,flags=re.M|re.S)
    text=re.sub(r"^\s{0,3}#{1,6}\s*|[*_~>#]","",text,flags=re.M)
    text=re.sub(r"\[([^]]+)\]\([^)]*\)",r"\1",text)
    text=re.sub(r"^\s*[-+•]\s*|^\s*\d+[.)]\s*","",text,flags=re.M).strip()
    chunks=[]
    for paragraph in [p.strip().replace("\n","") for p in text.splitlines() if p.strip()]:
        for sentence in re.split(r"(?<=[。！？!?])",paragraph):
            while len(sentence)>75:
                chunks.append(sentence[:75]); sentence=sentence[75:]
            if sentence.strip(): chunks.append(sentence.strip())
    if not chunks: raise ValueError("No narration text found")
    DIST.mkdir(exist_ok=True); parts=DIST/f"episode-{EPISODE:02d}-parts"; parts.mkdir(exist_ok=True)
    wavs=[]; captions=[]; elapsed=0.0
    def stamp(t):
        ms=int(round(t*1000)); h,ms=divmod(ms,3600000); m,ms=divmod(ms,60000); s,ms=divmod(ms,1000)
        return f"{h:02}:{m:02}:{s:02},{ms:03}"
    for i,chunk in enumerate(chunks,1):
        q=requests.post(API+"/audio_query",params={"text":chunk,"speaker":SPEAKER},timeout=60); q.raise_for_status()
        query=q.json(); query["speedScale"]=1.0
        a=requests.post(API+"/synthesis",params={"speaker":SPEAKER},json=query,timeout=120); a.raise_for_status()
        part=parts/f"{i:04d}.wav"; part.write_bytes(a.content); wavs.append(part)
        with wave.open(str(part),"rb") as w: duration=w.getnframes()/w.getframerate()
        captions.append(f"{i}\n{stamp(elapsed)} --> {stamp(elapsed+duration)}\n{chunk}\n"); elapsed+=duration
    audio=DIST/f"episode-{EPISODE:02d}.wav"
    with wave.open(str(wavs[0]),"rb") as first:
        params=first.getparams()
        with wave.open(str(audio),"wb") as out:
            out.setparams(params)
            for part in wavs:
                with wave.open(str(part),"rb") as w: out.writeframes(w.readframes(w.getnframes()))
    srt=DIST/f"episode-{EPISODE:02d}.srt"; srt.write_text("\n".join(captions),encoding="utf-8")
    video=DIST/f"episode-{EPISODE:02d}.mp4"
    vf=f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=white,subtitles='{srt.resolve()}':force_style='FontName=Noto Sans CJK JP,FontSize=30,Outline=2,Alignment=2,MarginV=70'"
    subprocess.run(["ffmpeg","-y","-loop","1","-framerate","30","-i",str(image),"-i",str(audio),"-vf",vf,"-c:v","libx264","-tune","stillimage","-pix_fmt","yuv420p","-c:a","aac","-b:a","192k","-shortest","-movflags","+faststart",str(video)],check=True)
    print(f"Created {video}")
if __name__=="__main__": main()
