#!/usr/bin/env python3
"""
Demo specjalne dla Claude i Moniki!
"""

import asyncio
import edge_tts
import pygame
from pathlib import Path

async def generate_greetings():
    text = "Cześć, jestem głosem który powstał dzięki Claude i Monice, witam serdecznie!"
    
    demos = [
        ("pl-PL-MarekNeural", "marek_normalny", "+0%", "+0Hz"),
        ("pl-PL-ZofiaNeural", "zofia_normalna", "+0%", "+0Hz"),
        ("pl-PL-MarekNeural", "marek_robot", "-10%", "-8Hz"),
        ("pl-PL-ZofiaNeural", "zofia_podekscytowana", "+20%", "+3Hz"),
        ("pl-PL-MarekNeural", "marek_chipmunk", "+40%", "+10Hz"),
        ("pl-PL-ZofiaNeural", "zofia_senna", "-30%", "-3Hz"),
    ]
    
    print("🎭 Generuję powitania od Claude i Moniki!\n")
    
    for voice, filename, rate, pitch in demos:
        print(f"🎤 Generuję: {filename}...")
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        output_path = f"output/{filename}.mp3"
        await communicate.save(output_path)
        print(f"✅ Zapisano: {output_path}")
    
    print("\n🎉 Wszystkie powitania wygenerowane!")
    print("\n🎧 Aby odsłuchać:")
    print("   open output/marek_normalny.mp3")
    print("   open output/zofia_podekscytowana.mp3")
    print("   open output/marek_chipmunk.mp3")

if __name__ == "__main__":
    asyncio.run(generate_greetings())