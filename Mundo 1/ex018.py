from math import radians, sin, cos, tan
an = float(input(' Digite o ângulo que você deseja: '))
co = cos(radians(an))
se = sin(radians(an))
ta = tan(radians(an))
print(' O ângulo de {} tem seno de {:.2f}.\n '
      'O ângulo de {} tem o cosseno de {:.2f}.\n '
      'O ângulo de {} tem a tangente de {:.2f}.'
      .format(an, se, an, co, an, ta))