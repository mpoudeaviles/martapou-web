#!/bin/bash
# Descarga todas las imágenes y vídeos del portfolio desde Cargo
# y las reduce a un máximo de 2400 px (para que la web cargue rápido).
# Hazlo ANTES de cancelar Cargo.

cd "$(dirname "$0")" || exit 1
echo "Descargando imágenes de Cargo..."

total=0; ok=0; fail=0
while IFS=$'\t' read -r name url; do
  [ -z "$name" ] && continue
  total=$((total+1))
  if [ -s "images/$name" ]; then ok=$((ok+1)); continue; fi
  if curl -fsSL --retry 3 -o "images/$name" "$url"; then
    ok=$((ok+1)); echo "  ✓ $name"
  else
    fail=$((fail+1)); echo "  ✗ $name"; rm -f "images/$name"
  fi
done < images/lista.txt

while IFS=$'\t' read -r name url; do
  [ -z "$name" ] && continue
  [ -s "media/$name" ] && continue
  echo "  vídeo: $name"
  curl -fsSL --retry 3 -o "media/$name" "$url" || echo "  ✗ $name"
done < media/lista.txt

echo ""
echo "Reduciendo imágenes grandes (máx. 2400 px)..."
for f in images/*; do
  case "$f" in *.txt) continue;; esac
  w=$(sips -g pixelWidth "$f" 2>/dev/null | awk '/pixelWidth/{print $2}')
  h=$(sips -g pixelHeight "$f" 2>/dev/null | awk '/pixelHeight/{print $2}')
  if [ -n "$w" ] && { [ "$w" -gt 2400 ] || [ "$h" -gt 2400 ]; }; then
    sips -Z 2400 "$f" >/dev/null 2>&1
  fi
done

echo ""
echo "Listo: $ok de $total imágenes descargadas ($fail fallos)."
[ "$fail" -gt 0 ] && echo "Si hay fallos, vuelve a ejecutar este archivo: solo baja las que faltan."
echo "Tamaño total:"; du -sh images media
echo ""
read -n 1 -s -r -p "Pulsa una tecla para cerrar"
