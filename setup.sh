#!/bin/bash

echo "🎭 Voice Shapeshifter - Setup"
echo "============================"

# Tworzenie środowiska wirtualnego
echo "📦 Tworzę środowisko wirtualne..."
python3 -m venv venv

# Aktywacja środowiska
echo "🔄 Aktywuję środowisko..."
source venv/bin/activate

# Instalacja zależności
echo "📚 Instaluję zależności..."
pip install --upgrade pip
pip install -r requirements.txt

# Próba instalacji CSM-MLX przez uv (jeśli dostępne)
if command -v uv &> /dev/null; then
    echo "🚀 Instaluję CSM-MLX przez uv..."
    uv pip install "csm-mlx[cli]"
else
    echo "📦 Instaluję CSM-MLX przez pip..."
    pip install csm-mlx
fi

echo ""
echo "✅ Setup zakończony!"
echo ""
echo "🎯 Aby rozpocząć:"
echo "   1. source venv/bin/activate"
echo "   2. python quick_demo.py      # dla szybkiego demo"
echo "   3. python voice_shapeshifter.py  # dla pełnego interfejsu"
echo ""
echo "🎤 Miłej zabawy z transformacją głosu!"