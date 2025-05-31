#!/usr/bin/env python3
"""
😈 Test nowych stylów
"""

import asyncio
import edge_tts

async def test_new_styles():
    text = "Cześć! Testujemy nowe style głosów. Jak brzmi ten?"
    voice = "pl-PL-MarekNeural"
    
    new_styles = {
        "demon": ("-50%", "-25Hz", "ULTRA niski demon z piekła"),
        "zmrozony": ("-15%", "+10Hz", "Drżący z zimna"),
        "kowboj": ("-10%", "-8Hz", "Howdy partner!"),
        "raper": ("+15%", "-5Hz", "Yo yo yo!")
    }
    
    print("😈 TESTOWANIE NOWYCH STYLÓW")
    print("=" * 50)
    
    for name, (rate, pitch, desc) in new_styles.items():
        print(f"\n🎤 {desc}")
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        filename = f"output/new_{name}.mp3"
        await communicate.save(filename)
        print(f"✅ {filename}")

if __name__ == "__main__":
    asyncio.run(test_new_styles())