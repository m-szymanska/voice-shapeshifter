#!/usr/bin/env python3
"""
🎭 Voice Shapeshifter - Generate Demo Voices
Generuje przykładowe głosy do katalogu 'output'
"""

import asyncio
import edge_tts
import os
from pathlib import Path

# Utwórz katalog output
output_dir = Path("output")
output_dir.mkdir(exist_ok=True)

async def generate_sample(text, voice, filename, style=None, rate="+0%", pitch="+0Hz"):
    """Generuj pojedynczy sample"""
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    output_path = output_dir / filename
    await communicate.save(str(output_path))
    print(f"✅ {filename}")
    return output_path

async def main():
    print("🎭 Voice Shapeshifter - Generowanie przykładów")
    print("=" * 50)
    
    # 1. Polski głos - różne wariacje
    print("\n📢 Polski głos (Marek) - różne style:")
    polish_text = "Cześć! Jestem Voice Shapeshifter. Potrafię mówić na wiele sposobów!"
    
    await generate_sample(polish_text, "pl-PL-MarekNeural", "pl_marek_normal.mp3")
    await generate_sample(polish_text, "pl-PL-MarekNeural", "pl_marek_fast.mp3", rate="+50%")
    await generate_sample(polish_text, "pl-PL-MarekNeural", "pl_marek_slow.mp3", rate="-30%")
    await generate_sample(polish_text, "pl-PL-MarekNeural", "pl_marek_high.mp3", pitch="+5Hz")
    await generate_sample(polish_text, "pl-PL-MarekNeural", "pl_marek_low.mp3", pitch="-5Hz")
    
    # 2. Polski głos kobiecy
    print("\n📢 Polski głos (Zofia):")
    await generate_sample(polish_text, "pl-PL-ZofiaNeural", "pl_zofia_normal.mp3")
    
    # 3. Angielski z emocjami
    print("\n🎭 Angielski głos (Jenny) - różne emocje:")
    english_voices = [
        ("This is amazing! I'm so happy!", "en_jenny_happy.mp3", "+10%", "+2Hz"),
        ("I feel a bit sad today...", "en_jenny_sad.mp3", "-10%", "-2Hz"),
        ("WATCH OUT! This is important!", "en_jenny_alert.mp3", "+20%", "+3Hz"),
        ("Psst... this is a secret...", "en_jenny_whisper.mp3", "-30%", "-3Hz"),
    ]
    
    for text, filename, rate, pitch in english_voices:
        await generate_sample(text, "en-US-JennyNeural", filename, rate=rate, pitch=pitch)
    
    # 4. Efekty specjalne
    print("\n🎨 Efekty specjalne (Guy):")
    special_text = "Hello! I can sound like different characters!"
    
    await generate_sample(special_text, "en-US-GuyNeural", "en_guy_robot.mp3", rate="-10%", pitch="-8Hz")
    await generate_sample(special_text, "en-US-GuyNeural", "en_guy_chipmunk.mp3", rate="+40%", pitch="+8Hz")
    await generate_sample(special_text, "en-US-GuyNeural", "en_guy_giant.mp3", rate="-20%", pitch="-10Hz")
    
    # 5. Wielojęzyczność
    print("\n🌍 Przykłady wielojęzyczne:")
    languages = [
        ("fr-FR-HenriNeural", "Bonjour! Je suis Voice Shapeshifter!", "fr_henri.mp3"),
        ("de-DE-ConradNeural", "Hallo! Ich bin Voice Shapeshifter!", "de_conrad.mp3"),
        ("es-ES-AlvaroNeural", "¡Hola! Soy Voice Shapeshifter!", "es_alvaro.mp3"),
        ("ja-JP-NanamiNeural", "こんにちは！私はボイスシェイプシフターです！", "ja_nanami.mp3"),
    ]
    
    for voice, text, filename in languages:
        await generate_sample(text, voice, filename)
    
    print(f"\n✨ Gotowe! Wygenerowano {len(list(output_dir.glob('*.mp3')))} plików w katalogu 'output/'")
    print("\n🎧 Możesz teraz odsłuchać pliki MP3!")
    
    # Pokaż listę plików
    print("\n📂 Lista wygenerowanych plików:")
    for mp3_file in sorted(output_dir.glob("*.mp3")):
        size_kb = mp3_file.stat().st_size / 1024
        print(f"  • {mp3_file.name} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    asyncio.run(main())