#!/usr/bin/env python3
"""
🎪 Test ekstremalnych stylów głosów
"""

import asyncio
import edge_tts
from pathlib import Path

# Ekstremalne style
EXTREME_STYLES = {
    "normalny": ("+0%", "+0Hz"),
    "robot": ("-25%", "-12Hz"),
    "wiewiorka": ("+80%", "+20Hz"),
    "gigant": ("-40%", "-20Hz"),
    "duch": ("-30%", "+15Hz"),
    "dziecko": ("+50%", "+25Hz"),
    "turbo": ("+100%", "+5Hz"),
}

async def test_styles():
    """Testuj wszystkie style z tym samym tekstem"""
    
    text = "Cześć! To jest test ekstremalnych stylów głosu. Czy słyszysz różnicę?"
    voice = "pl-PL-MarekNeural"
    
    print("🎪 TESTOWANIE EKSTREMALNYCH STYLÓW")
    print("=" * 50)
    
    for style_name, (rate, pitch) in EXTREME_STYLES.items():
        print(f"\n🎤 Generuję styl: {style_name} (rate={rate}, pitch={pitch})")
        
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        filename = f"output/test_{style_name}.mp3"
        await communicate.save(filename)
        print(f"✅ Zapisano: {filename}")
    
    print("\n\n📊 PORÓWNANIE STYLÓW:")
    print("-" * 50)
    print("STYL         | PRĘDKOŚĆ | WYSOKOŚĆ | EFEKT")
    print("-" * 50)
    print("Normalny     |    0%    |    0Hz   | Bazowy głos")
    print("Robot        |  -25%    |  -12Hz   | Mechaniczny, głęboki")
    print("Wiewiórka    |  +80%    |  +20Hz   | SUPER szybki i wysoki")
    print("Gigant       |  -40%    |  -20Hz   | MEGA wolny i niski")
    print("Duch         |  -30%    |  +15Hz   | Wolny ale wysoki (upiorny)")
    print("Dziecko      |  +50%    |  +25Hz   | Bardzo wysoki i szybki")
    print("Turbo        | +100%    |   +5Hz   | ULTRA szybki")
    
    print("\n🎧 Odsłuchaj pliki w kolejności żeby usłyszeć różnice!")
    print("\nPROTIP: Najlepsze efekty:")
    print("  • Wiewiórka vs Gigant - totalnie różne!")
    print("  • Robot vs Dziecko - mechaniczny vs słodki")
    print("  • Duch - upiorny efekt (wolny ale wysoki)")

if __name__ == "__main__":
    Path("output").mkdir(exist_ok=True)
    asyncio.run(test_styles())