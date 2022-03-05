# Pengguna paket dapat mengimpor modul individual dari paket
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# Cara alternatif mengimpor submodule adalah:
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)

# mengimpor fungsi atau variabel yang diinginkan secara langsung:
from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)
