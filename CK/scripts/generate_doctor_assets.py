import os
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parents[1] / 'assets' / 'characters' / 'doctors'
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Common helper for SVG header
def svg_wrap(content):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 480" width="360" height="480">
  <defs>
    <filter id="glow-gold" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="glow-fire" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="glow-green" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="7" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <linearGradient id="knife-blade" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#d9e2ec"/>
      <stop offset="100%" stop-color="#9fb3c8"/>
    </linearGradient>
    <linearGradient id="wok-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#334e68"/>
      <stop offset="100%" stop-color="#102a43"/>
    </linearGradient>
    <linearGradient id="flame-grad" x1="0" y1="1" x2="0" y2="0">
      <stop offset="0%" stop-color="#d84c38"/>
      <stop offset="50%" stop-color="#f38b4a"/>
      <stop offset="100%" stop-color="#f7d070"/>
    </linearGradient>
    <linearGradient id="rx-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#347d69"/>
      <stop offset="100%" stop-color="#8ac6a7"/>
    </linearGradient>
  </defs>
{content}
</svg>'''

# -------------------------------------------------------------
# DR. SPEED (快刀醫師)
# Palette: Skin #e6b88a, Hair #20252d, Coat #f8fbff, Tie/Accents #f3b84a, Pants #102a43
# Glasses: Rectangular / stylish frames
# -------------------------------------------------------------

def speed_head(cx=180, cy=110, expr='smile'):
    mouth = f'<path d="M{cx-18} {cy+28} Q{cx} {cy+40} {cx+18} {cy+28}" fill="none" stroke="#7a4b3f" stroke-width="3.5" stroke-linecap="round"/>'
    if expr == 'open':
        mouth = f'<path d="M{cx-18} {cy+24} Q{cx} {cy+42} {cx+18} {cy+24} Z" fill="#7a4b3f"/><path d="M{cx-12} {cy+25} Q{cx} {cy+33} {cx+12} {cy+25}" fill="#ffffff"/>'
    elif expr == 'focus':
        mouth = f'<path d="M{cx-14} {cy+28} H{cx+14}" fill="none" stroke="#7a4b3f" stroke-width="3.5" stroke-linecap="round"/>'
    
    return f'''
    <!-- Head & Hair -->
    <circle cx="{cx}" cy="{cy}" r="46" fill="#e6b88a"/>
    <!-- Energetic swooping hair -->
    <path d="M{cx-46} {cy-10} Q{cx-40} {cy-50} {cx} {cy-52} Q{cx+44} {cy-50} {cx+48} {cy-8} Q{cx+30} {cy-25} {cx+8} {cy-22} Q{cx-24} {cy-20} {cx-46} {cy-10} Z" fill="#20252d"/>
    <path d="M{cx-20} {cy-45} Q{cx-10} {cy-62} {cx+15} {cy-50} Q{cx-5} {cy-48} {cx-20} {cy-45} Z" fill="#334050"/>
    <!-- Eyes -->
    <circle cx="{cx-18}" cy="{cy+2}" r="4" fill="#102a43"/>
    <circle cx="{cx+18}" cy="{cy+2}" r="4" fill="#102a43"/>
    <!-- Glasses -->
    <g fill="none" stroke="#26394c" stroke-width="3.5">
      <rect x="{cx-36}" cy="{cy-10}" width="28" height="22" rx="7"/>
      <rect x="{cx+8}" cy="{cy-10}" width="28" height="22" rx="7"/>
      <path d="M{cx-8} {cy} H{cx+8}"/>
    </g>
    <!-- Eyebrows -->
    <path d="M{cx-32} {cy-16} Q{cx-20} {cy-22} {cx-8} {cy-18}" fill="none" stroke="#20252d" stroke-width="3" stroke-linecap="round"/>
    <path d="M{cx+8} {cy-18} Q{cx+20} {cy-22} {cx+32} {cy-16}" fill="none" stroke="#20252d" stroke-width="3" stroke-linecap="round"/>
    {mouth}
    '''

def speed_legs(lx1=155, lx2=205, y=360, ey=460):
    return f'''
    <!-- Legs & Shoes -->
    <path d="M{lx1-12} {y} L{lx1-16} {ey-18} H{lx1+12} L{lx1+16} {y} Z" fill="#102a43"/>
    <path d="M{lx2-16} {y} L{lx2-12} {ey-18} H{lx2+16} L{lx2+12} {y} Z" fill="#102a43"/>
    <rect x="{lx1-24}" y="{ey-18}" width="38" height="18" rx="8" fill="#1e3a5f"/>
    <rect x="{lx2-14}" y="{ey-18}" width="38" height="18" rx="8" fill="#1e3a5f"/>
    '''

def speed_coat_body(cx=180, cy=240):
    return f'''
    <!-- Torso: Lab coat over shirt & tie -->
    <path d="M{cx-46} {cy-80} L{cx-54} {cy+120} H{cx+54} L{cx+46} {cy-80} Z" fill="#f8fbff" stroke="#d9e2ec" stroke-width="2"/>
    <path d="M{cx-24} {cy-80} L{cx} {cy-35} L{cx+24} {cy-80} Z" fill="#eceff1"/>
    <!-- Yellow tie -->
    <polygon points="{cx-6},{cy-40} {cx+6},{cy-40} {cx+9},{cy+40} {cx},{cy+55} {cx-9},{cy+40}" fill="#f3b84a"/>
    <!-- Coat lapels -->
    <path d="M{cx-46} {cy-80} L{cx-18} {cy-15} L{cx-36} {cy+45} L{cx-48} {cy+120}" fill="none" stroke="#cfd8dc" stroke-width="2.5"/>
    <path d="M{cx+46} {cy-80} L{cx+18} {cy-15} L{cx+36} {cy+45} L{cx+48} {cy+120}" fill="none" stroke="#cfd8dc" stroke-width="2.5"/>
    '''

# ----------------- Dr Speed States -----------------

def make_speed_idle():
    content = f'''
    <g id="speed-idle">
      {speed_legs()}
      {speed_coat_body()}
      <!-- Left arm holding prep tray -->
      <path d="M134 175 Q95 210 90 260 L120 270 Q125 220 152 195 Z" fill="#f8fbff"/>
      <rect x="52" y="250" width="75" height="16" rx="5" fill="#cfd8dc" stroke="#90a4ae" stroke-width="2"/>
      <circle cx="70" cy="245" r="7" fill="#ffffff" stroke="#90a4ae"/>
      <circle cx="90" cy="244" r="8" fill="#48bb78"/>
      <circle cx="110" cy="245" r="7" fill="#e53e3e"/>
      <circle cx="98" cy="265" r="9" fill="#e6b88a"/>
      <!-- Right arm holding quick chef knife -->
      <path d="M226 175 Q265 205 270 250 L242 260 Q236 220 208 195 Z" fill="#f8fbff"/>
      <circle cx="265" cy="254" r="9" fill="#e6b88a"/>
      <rect x="264" y="248" width="14" height="8" rx="2" fill="#8d6e63"/>
      <path d="M278 245 L320 240 L315 260 L278 255 Z" fill="url(#knife-blade)" stroke="#9fb3c8" stroke-width="1.5"/>
      {speed_head(180, 110, 'smile')}
    </g>
    '''
    return svg_wrap(content)

def make_speed_entrance():
    content = f'''
    <g id="speed-entrance">
      <!-- Speed dash trails & dust -->
      <g opacity="0.75">
        <path d="M10 390 H90 M25 410 H130 M5 430 H80" stroke="#f3b84a" stroke-width="4" stroke-linecap="round"/>
        <path d="M40 370 H110 M20 350 H85" stroke="#ffe082" stroke-width="3" stroke-linecap="round"/>
        <circle cx="100" cy="425" r="14" fill="#f3b84a" opacity="0.3"/>
        <circle cx="125" cy="405" r="9" fill="#f3b84a" opacity="0.4"/>
      </g>
      <!-- Dynamic sliding pose -->
      <g transform="rotate(-6 180 240)">
        {speed_legs(140, 220, 360, 450)}
        {speed_coat_body(180, 230)}
        <!-- Left arm thrust forward holding tray -->
        <path d="M134 165 Q70 170 50 195 L65 215 Q95 195 145 185 Z" fill="#f8fbff"/>
        <rect x="25" y="180" width="80" height="18" rx="6" fill="#cfd8dc" stroke="#90a4ae" stroke-width="2"/>
        <circle cx="50" cy="175" r="8" fill="#48bb78"/>
        <circle cx="75" cy="174" r="8" fill="#ffffff" stroke="#90a4ae"/>
        <circle cx="60" cy="202" r="9" fill="#e6b88a"/>
        <!-- Right arm swinging knife in flair -->
        <path d="M226 165 Q275 160 305 130 L320 145 Q285 185 215 190 Z" fill="#f8fbff"/>
        <circle cx="310" cy="132" r="9" fill="#e6b88a"/>
        <path d="M316 128 L350 90 L342 82 L310 120 Z" fill="url(#knife-blade)" stroke="#9fb3c8" stroke-width="1.5"/>
        <path d="M340 75 L355 95 L335 90 Z" fill="#ffe082"/>
        {speed_head(180, 100, 'open')}
      </g>
    </g>
    '''
    return svg_wrap(content)

def make_speed_prep():
    content = f'''
    <g id="speed-prep">
      <!-- Cutting board / prep table front -->
      <rect x="40" y="310" width="280" height="42" rx="10" fill="#e2d4be" stroke="#bfa98b" stroke-width="3"/>
      <rect x="70" y="318" width="80" height="24" rx="4" fill="#ffffff" opacity="0.85"/>
      <circle cx="200" cy="328" r="10" fill="#48bb78"/>
      <circle cx="225" cy="328" r="9" fill="#e53e3e"/>
      <circle cx="250" cy="330" r="12" fill="#a0aec0"/>
      {speed_legs(160, 200, 350, 460)}
      {speed_coat_body(180, 235)}
      <!-- Left hand stabilizing tofu block -->
      <path d="M135 170 Q105 230 110 295 L132 298 Q128 240 155 190 Z" fill="#f8fbff"/>
      <circle cx="112" cy="305" r="9" fill="#e6b88a"/>
      <rect x="95" y="312" width="26" height="20" rx="3" fill="#ffffff" stroke="#cbd5e0" stroke-width="2"/>
      <!-- Right hand holding knife in fast rhythm -->
      <path d="M225 170 Q255 220 240 280 L218 275 Q230 225 205 190 Z" fill="#f8fbff"/>
      <circle cx="236" cy="285" r="9" fill="#e6b88a"/>
      <path d="M236 280 L250 318 L235 320 L226 285 Z" fill="url(#knife-blade)" stroke="#9fb3c8" stroke-width="1.5"/>
      <!-- Action lines around knife -->
      <path d="M245 270 L260 260 M255 285 L275 280 M248 300 L268 302" stroke="#f3b84a" stroke-width="3" stroke-linecap="round"/>
      {speed_head(180, 110, 'focus')}
    </g>
    '''
    return svg_wrap(content)

def make_speed_cut():
    content = f'''
    <g id="speed-cut">
      <!-- Cutting motion blur and diced cubes flying -->
      <g opacity="0.85">
        <rect x="80" y="270" width="18" height="18" rx="3" fill="#ffffff" stroke="#cbd5e0" stroke-width="1.5" transform="rotate(15 89 279)"/>
        <rect x="130" y="240" width="16" height="16" rx="3" fill="#ffffff" stroke="#cbd5e0" stroke-width="1.5" transform="rotate(-20 138 248)"/>
        <rect x="235" y="250" width="16" height="16" rx="3" fill="#ffffff" stroke="#cbd5e0" stroke-width="1.5" transform="rotate(35 243 258)"/>
        <circle cx="170" cy="235" r="6" fill="#48bb78"/>
        <circle cx="195" cy="225" r="5" fill="#48bb78"/>
        <circle cx="210" cy="245" r="6" fill="#48bb78"/>
      </g>
      <!-- Cutting arcs -->
      <path d="M120 280 Q180 230 240 280" fill="none" stroke="#f3b84a" stroke-width="4" stroke-dasharray="6,4"/>
      <path d="M135 295 Q180 250 225 295" fill="none" stroke="#ffe082" stroke-width="3"/>
      {speed_legs(150, 210, 360, 460)}
      {speed_coat_body(180, 235)}
      <!-- High speed dual knife flurry! -->
      <!-- Left knife thrust -->
      <path d="M135 170 Q110 210 130 250 L110 258 Q90 215 120 175 Z" fill="#f8fbff"/>
      <circle cx="132" cy="255" r="9" fill="#e6b88a"/>
      <path d="M136 250 L155 285 L145 288 L130 255 Z" fill="url(#knife-blade)" stroke="#9fb3c8" stroke-width="1.5"/>
      <!-- Right knife downstroke -->
      <path d="M225 170 Q250 205 230 255 L210 250 Q230 210 205 175 Z" fill="#f8fbff"/>
      <circle cx="228" cy="256" r="9" fill="#e6b88a"/>
      <path d="M228 252 L210 290 L200 285 L222 250 Z" fill="url(#knife-blade)" stroke="#9fb3c8" stroke-width="1.5"/>
      {speed_head(180, 105, 'open')}
    </g>
    '''
    return svg_wrap(content)

def make_speed_cook():
    content = f'''
    <g id="speed-cook">
      <!-- Wok and quick stirring action -->
      <ellipse cx="180" cy="330" rx="90" ry="34" fill="url(#wok-grad)"/>
      <ellipse cx="180" cy="328" rx="84" ry="30" fill="#2d3748"/>
      <!-- Mapo tofu simmering inside -->
      <ellipse cx="180" cy="328" rx="72" ry="24" fill="#c53030"/>
      <rect x="150" y="320" width="14" height="12" rx="2" fill="#fff"/>
      <rect x="175" y="322" width="12" height="12" rx="2" fill="#fff"/>
      <rect x="195" y="318" width="13" height="12" rx="2" fill="#fff"/>
      <circle cx="165" cy="325" r="4" fill="#48bb78"/>
      <circle cx="190" cy="324" r="4" fill="#48bb78"/>
      <!-- Quick wok steam & snap sparks -->
      <path d="M145 310 Q140 280 150 260" stroke="#ffffff" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.7"/>
      <path d="M180 305 Q185 275 175 255" stroke="#ffffff" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.8"/>
      <path d="M215 310 Q220 280 210 260" stroke="#ffffff" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.7"/>
      <circle cx="160" cy="285" r="3" fill="#f3b84a"/>
      <circle cx="205" cy="280" r="3" fill="#f3b84a"/>
      {speed_legs(150, 210, 360, 460)}
      {speed_coat_body(180, 230)}
      <!-- Hands holding wok handle and ladle -->
      <path d="M135 170 Q85 230 100 310 L120 315 Q110 240 155 185 Z" fill="#f8fbff"/>
      <circle cx="98" cy="312" r="9" fill="#e6b88a"/>
      <rect x="70" y="306" width="32" height="10" rx="4" fill="#8d6e63"/>
      <!-- Right hand with metal spatula/ladle -->
      <path d="M225 170 Q270 230 235 295 L215 288 Q240 235 205 185 Z" fill="#f8fbff"/>
      <circle cx="236" cy="296" r="9" fill="#e6b88a"/>
      <path d="M236 295 L200 330" stroke="#a0aec0" stroke-width="5" stroke-linecap="round"/>
      {speed_head(180, 105, 'focus')}
    </g>
    '''
    return svg_wrap(content)

def make_speed_serve():
    content = f'''
    <g id="speed-serve">
      <!-- Proud serving presentation with sparkling plate -->
      {speed_legs(155, 205, 360, 460)}
      {speed_coat_body(180, 235)}
      <!-- Both arms presenting plate forward -->
      <path d="M135 175 Q120 230 145 280 L165 275 Q145 230 155 185 Z" fill="#f8fbff"/>
      <circle cx="146" cy="285" r="9" fill="#e6b88a"/>
      <path d="M225 175 Q240 230 215 280 L195 275 Q215 230 205 185 Z" fill="#f8fbff"/>
      <circle cx="214" cy="285" r="9" fill="#e6b88a"/>
      <!-- Porcelain bowl of Mapo Tofu -->
      <ellipse cx="180" cy="285" rx="55" ry="18" fill="#ffffff" stroke="#cbd5e0" stroke-width="2"/>
      <ellipse cx="180" cy="282" rx="46" ry="13" fill="#c53030"/>
      <rect x="160" y="277" width="10" height="9" rx="2" fill="#ffffff"/>
      <rect x="178" y="278" width="10" height="9" rx="2" fill="#ffffff"/>
      <rect x="195" y="276" width="9" height="9" rx="2" fill="#ffffff"/>
      <circle cx="170" cy="280" r="3" fill="#48bb78"/>
      <circle cx="188" cy="279" r="3" fill="#48bb78"/>
      <!-- Aroma swirls and sparkles -->
      <path d="M165 260 Q160 235 172 215" stroke="#ffffff" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.9"/>
      <path d="M195 260 Q200 235 188 215" stroke="#ffffff" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.9"/>
      <!-- Sparkles -->
      <path d="M120 230 L125 240 L135 245 L125 250 L120 260 L115 250 L105 245 L115 240 Z" fill="#f3b84a"/>
      <path d="M240 230 L245 240 L255 245 L245 250 L240 260 L235 250 L225 245 L235 240 Z" fill="#f3b84a"/>
      {speed_head(180, 105, 'smile')}
    </g>
    '''
    return svg_wrap(content)

def make_speed_ultimate():
    content = f'''
    <g id="speed-ultimate">
      <!-- 閃電備料: Lightning bolts, electric aura, afterimage blur -->
      <!-- Electric shockwaves -->
      <g filter="url(#glow-gold)">
        <circle cx="180" cy="240" r="150" fill="none" stroke="#f3b84a" stroke-width="4" stroke-dasharray="14,10" opacity="0.6"/>
        <path d="M60 120 L110 200 L85 220 L150 320" stroke="#f7d070" stroke-width="5" fill="none" stroke-linecap="round"/>
        <path d="M300 130 L250 210 L275 230 L210 330" stroke="#f7d070" stroke-width="5" fill="none" stroke-linecap="round"/>
        <path d="M120 60 L150 120 L135 135 L190 200" stroke="#ffe082" stroke-width="4" fill="none"/>
        <path d="M240 60 L210 120 L225 135 L170 200" stroke="#ffe082" stroke-width="4" fill="none"/>
      </g>
      <!-- Speed aura silhouette -->
      <g opacity="0.35" transform="translate(-18, 0)">
        {speed_legs(145, 215, 360, 460)}
        {speed_coat_body(180, 235)}
      </g>
      <g opacity="0.35" transform="translate(18, 0)">
        {speed_legs(145, 215, 360, 460)}
        {speed_coat_body(180, 235)}
      </g>
      <!-- Main character with dynamic lightning knife pose -->
      {speed_legs(145, 215, 360, 460)}
      {speed_coat_body(180, 235)}
      <!-- Knives radiating electricity -->
      <path d="M135 170 Q70 190 75 250 L95 255 Q95 205 145 185 Z" fill="#f8fbff"/>
      <circle cx="76" cy="254" r="9" fill="#e6b88a"/>
      <path d="M72 250 L40 280 L32 272 L65 245 Z" fill="#fff" stroke="#f3b84a" stroke-width="2.5"/>
      <path d="M225 170 Q290 190 285 250 L265 255 Q265 205 215 185 Z" fill="#f8fbff"/>
      <circle cx="284" cy="254" r="9" fill="#e6b88a"/>
      <path d="M288 250 L320 280 L328 272 L295 245 Z" fill="#fff" stroke="#f3b84a" stroke-width="2.5"/>
      {speed_head(180, 105, 'open')}
      <!-- Kanji banner badge: 閃電備料 -->
      <rect x="90" y="420" width="180" height="38" rx="19" fill="#102a43" stroke="#f3b84a" stroke-width="3"/>
      <text x="180" y="445" font-family="sans-serif" font-size="20" font-weight="900" fill="#f3b84a" text-anchor="middle" letter-spacing="4">⚡ 閃電備料 ⚡</text>
    </g>
    '''
    return svg_wrap(content)

# -------------------------------------------------------------
# DR. HEAT (火候醫師)
# Palette: Skin #d8a77a, Hair #1e242b, Coat #f8fbff, Shirt #8ba8c4, Tie #e85d4a, Pants #102a43
# Wok master, calm, flame flourish
# -------------------------------------------------------------

def heat_head(cx=180, cy=110, expr='calm'):
    mouth = f'<path d="M{cx-14} {cy+28} Q{cx} {cy+35} {cx+14} {cy+28}" fill="none" stroke="#7a4b3f" stroke-width="3.5" stroke-linecap="round"/>'
    if expr == 'smile':
        mouth = f'<path d="M{cx-16} {cy+26} Q{cx} {cy+38} {cx+16} {cy+26}" fill="none" stroke="#7a4b3f" stroke-width="3.5" stroke-linecap="round"/>'
    elif expr == 'focus':
        mouth = f'<path d="M{cx-12} {cy+28} H{cx+12}" fill="none" stroke="#7a4b3f" stroke-width="3.5" stroke-linecap="round"/>'
    
    return f'''
    <!-- Head & Hair -->
    <circle cx="{cx}" cy="{cy}" r="46" fill="#d8a77a"/>
    <!-- Neat, mature combed hair -->
    <path d="M{cx-46} {cy-6} Q{cx-42} {cy-52} {cx} {cy-50} Q{cx+44} {cy-48} {cx+46} {cy-4} Q{cx+24} {cy-22} {cx} {cy-24} Q{cx-24} {cy-24} {cx-46} {cy-6} Z" fill="#1e242b"/>
    <!-- Eyes -->
    <circle cx="{cx-17}" cy="{cy+2}" r="4" fill="#102a43"/>
    <circle cx="{cx+17}" cy="{cy+2}" r="4" fill="#102a43"/>
    <!-- Eyebrows -->
    <path d="M{cx-28} {cy-14} H{cx-8}" fill="none" stroke="#1e242b" stroke-width="3.5" stroke-linecap="round"/>
    <path d="M{cx+8} {cy-14} H{cx+28}" fill="none" stroke="#1e242b" stroke-width="3.5" stroke-linecap="round"/>
    <!-- Glasses -->
    <g fill="none" stroke="#26394c" stroke-width="3.5">
      <rect x="{cx-34}" cy="{cy-10}" width="26" height="22" rx="6"/>
      <rect x="{cx+8}" cy="{cy-10}" width="26" height="22" rx="6"/>
      <path d="M{cx-8} {cy+1} H{cx+8}"/>
    </g>
    {mouth}
    '''

def heat_coat_body(cx=180, cy=240):
    return f'''
    <!-- Torso: Lab coat over blue shirt & red flame tie -->
    <path d="M{cx-48} {cy-80} L{cx-54} {cy+120} H{cx+54} L{cx+48} {cy-80} Z" fill="#f8fbff" stroke="#d9e2ec" stroke-width="2"/>
    <path d="M{cx-24} {cy-80} L{cx} {cy-35} L{cx+24} {cy-80} Z" fill="#8ba8c4"/>
    <!-- Red tie -->
    <polygon points="{cx-6},{cy-40} {cx+6},{cy-40} {cx+9},{cy+40} {cx},{cy+55} {cx-9},{cy+40}" fill="#e85d4a"/>
    <!-- Coat lapels -->
    <path d="M{cx-48} {cy-80} L{cx-18} {cy-15} L{cx-36} {cy+45} L{cx-48} {cy+120}" fill="none" stroke="#cfd8dc" stroke-width="2.5"/>
    <path d="M{cx+48} {cy-80} L{cx+18} {cy-15} L{cx+36} {cy+45} L{cx+48} {cy+120}" fill="none" stroke="#cfd8dc" stroke-width="2.5"/>
    '''

# ----------------- Dr Heat States -----------------

def make_heat_idle():
    content = f'''
    <g id="heat-idle">
      {speed_legs(150, 210, 360, 460)}
      {heat_coat_body()}
      <!-- Left arm holding iron wok at side -->
      <path d="M132 175 Q90 220 95 280 L120 285 Q115 235 150 190 Z" fill="#f8fbff"/>
      <circle cx="102" cy="290" r="9" fill="#d8a77a"/>
      <ellipse cx="65" cy="300" rx="35" ry="42" fill="url(#wok-grad)"/>
      <ellipse cx="65" cy="300" rx="28" ry="34" fill="#2d3748"/>
      <!-- Right arm holding spice bottle -->
      <path d="M228 175 Q265 215 255 265 L232 268 Q240 225 210 190 Z" fill="#f8fbff"/>
      <circle cx="250" cy="272" r="9" fill="#d8a77a"/>
      <rect x="242" y="248" width="16" height="28" rx="4" fill="#e85d4a" stroke="#ffffff" stroke-width="1.5"/>
      <rect x="246" y="240" width="8" height="8" rx="2" fill="#e2e8f0"/>
      {heat_head(180, 110, 'calm')}
    </g>
    '''
    return svg_wrap(content)

def make_heat_entrance():
    content = f'''
    <g id="heat-entrance">
      <!-- Flame ignite sparks from wok spatula -->
      <g filter="url(#glow-fire)">
        <path d="M240 180 Q255 130 245 100 Q270 140 280 180 Q260 210 240 180 Z" fill="url(#flame-grad)"/>
        <circle cx="260" cy="115" r="5" fill="#f7d070"/>
        <circle cx="280" cy="140" r="4" fill="#f38b4a"/>
      </g>
      {speed_legs(145, 215, 360, 460)}
      {heat_coat_body(180, 235)}
      <!-- Left arm holding iron wok forward with authority -->
      <path d="M132 175 Q80 190 70 240 L92 245 Q100 210 148 185 Z" fill="#f8fbff"/>
      <circle cx="78" cy="246" r="9" fill="#d8a77a"/>
      <ellipse cx="60" cy="255" rx="38" ry="24" fill="url(#wok-grad)"/>
      <!-- Right arm raising spatula with ignite flame -->
      <path d="M228 175 Q275 190 260 150 L240 155 Q250 195 210 185 Z" fill="#f8fbff"/>
      <circle cx="256" cy="152" r="9" fill="#d8a77a"/>
      <rect x="252" y="140" width="8" height="40" rx="3" fill="#a0aec0" transform="rotate(-25 256 160)"/>
      {heat_head(180, 105, 'smile')}
    </g>
    '''
    return svg_wrap(content)

def make_heat_prep():
    content = f'''
    <g id="heat-prep">
      <!-- Prep station inspecting doubanjiang -->
      <rect x="50" y="320" width="260" height="38" rx="8" fill="#e2d4be" stroke="#bfa98b" stroke-width="2.5"/>
      {speed_legs(155, 205, 355, 460)}
      {heat_coat_body(180, 235)}
      <!-- Left hand steadying spice jar -->
      <path d="M135 175 Q115 235 125 295 L145 292 Q135 240 155 190 Z" fill="#f8fbff"/>
      <circle cx="128" cy="302" r="9" fill="#d8a77a"/>
      <rect x="115" y="295" width="24" height="32" rx="4" fill="#9b2c2c" stroke="#fff" stroke-width="1.5"/>
      <text x="127" y="316" font-size="10" font-family="sans-serif" font-weight="bold" fill="#fff" text-anchor="middle">醬</text>
      <!-- Right hand holding precision spoon -->
      <path d="M225 175 Q245 235 215 285 L198 280 Q225 235 205 190 Z" fill="#f8fbff"/>
      <circle cx="212" cy="290" r="9" fill="#d8a77a"/>
      <path d="M212 290 L185 315" stroke="#a0aec0" stroke-width="4" stroke-linecap="round"/>
      <circle cx="180" cy="318" r="6" fill="#c53030"/>
      {heat_head(180, 110, 'focus')}
    </g>
    '''
    return svg_wrap(content)

def make_heat_cut():
    content = f'''
    <g id="heat-cut">
      <!-- Steady, precise knife cutting with squared grid lines -->
      <rect x="50" y="320" width="260" height="38" rx="8" fill="#e2d4be" stroke="#bfa98b" stroke-width="2.5"/>
      <rect x="120" y="312" width="50" height="24" rx="3" fill="#ffffff" stroke="#cbd5e0" stroke-width="2"/>
      <!-- Grid measurement overlay -->
      <path d="M132 312 V336 M145 312 V336 M158 312 V336" stroke="#4a5568" stroke-width="1.5" stroke-dasharray="2,2"/>
      {speed_legs(155, 205, 355, 460)}
      {heat_coat_body(180, 235)}
      <!-- Left hand guide -->
      <path d="M135 175 Q115 230 130 295 L150 290 Q135 240 155 190 Z" fill="#f8fbff"/>
      <circle cx="132" cy="300" r="9" fill="#d8a77a"/>
      <!-- Right hand vertical cleaver downstroke -->
      <path d="M225 175 Q250 220 220 275 L200 270 Q230 220 205 190 Z" fill="#f8fbff"/>
      <circle cx="216" cy="282" r="9" fill="#d8a77a"/>
      <rect x="210" y="275" width="12" height="42" rx="2" fill="url(#knife-blade)" stroke="#9fb3c8" stroke-width="1.5"/>
      {heat_head(180, 110, 'focus')}
    </g>
    '''
    return svg_wrap(content)

def make_heat_cook():
    content = f'''
    <g id="heat-cook">
      <!-- Masterful wok flame burst -->
      <g filter="url(#glow-fire)">
        <path d="M110 320 Q100 250 140 210 Q160 250 180 200 Q200 260 220 220 Q240 270 250 320 Z" fill="url(#flame-grad)" opacity="0.85"/>
      </g>
      <!-- Heavy wok tossed at dynamic tilt -->
      <g transform="rotate(-10 180 320)">
        <ellipse cx="180" cy="320" rx="85" ry="32" fill="url(#wok-grad)"/>
        <ellipse cx="180" cy="318" rx="78" ry="26" fill="#2d3748"/>
        <ellipse cx="180" cy="318" rx="68" ry="20" fill="#c53030"/>
        <rect x="155" y="312" width="14" height="12" rx="2" fill="#ffffff"/>
        <rect x="180" y="314" width="14" height="12" rx="2" fill="#ffffff"/>
        <circle cx="170" cy="316" r="4" fill="#48bb78"/>
      </g>
      {speed_legs(145, 215, 360, 460)}
      {heat_coat_body(180, 235)}
      <!-- Steady left hand holding wok loop handle -->
      <path d="M132 175 Q85 220 100 290 L120 295 Q110 230 152 185 Z" fill="#f8fbff"/>
      <circle cx="102" cy="296" r="9" fill="#d8a77a"/>
      <!-- Right hand tossing with ladle -->
      <path d="M228 175 Q265 210 240 270 L218 265 Q240 220 208 185 Z" fill="#f8fbff"/>
      <circle cx="236" cy="275" r="9" fill="#d8a77a"/>
      <path d="M236 275 L205 315" stroke="#a0aec0" stroke-width="5" stroke-linecap="round"/>
      {heat_head(180, 105, 'focus')}
    </g>
    '''
    return svg_wrap(content)

def make_heat_serve():
    content = f'''
    <g id="heat-serve">
      <!-- Careful presentation of steaming aromatic wok bowl -->
      {speed_legs(155, 205, 360, 460)}
      {heat_coat_body(180, 235)}
      <!-- Both hands holding heavy black ceramic bowl -->
      <path d="M135 175 Q115 230 145 285 L165 280 Q140 230 155 185 Z" fill="#f8fbff"/>
      <circle cx="148" cy="290" r="9" fill="#d8a77a"/>
      <path d="M225 175 Q245 230 215 285 L195 280 Q220 230 205 185 Z" fill="#f8fbff"/>
      <circle cx="212" cy="290" r="9" fill="#d8a77a"/>
      <!-- Ceramic dish -->
      <ellipse cx="180" cy="290" rx="58" ry="20" fill="#2d3748" stroke="#f3b84a" stroke-width="2.5"/>
      <ellipse cx="180" cy="286" rx="48" ry="14" fill="#c53030"/>
      <rect x="160" y="280" width="12" height="10" rx="2" fill="#ffffff"/>
      <rect x="180" y="282" width="12" height="10" rx="2" fill="#ffffff"/>
      <circle cx="172" cy="284" r="4" fill="#48bb78"/>
      <circle cx="192" cy="285" r="4" fill="#48bb78"/>
      <!-- Fragrant steam curls -->
      <path d="M160 260 Q150 225 170 200" stroke="#ffffff" stroke-width="3.5" stroke-linecap="round" fill="none" opacity="0.8"/>
      <path d="M200 260 Q210 225 190 200" stroke="#ffffff" stroke-width="3.5" stroke-linecap="round" fill="none" opacity="0.8"/>
      {heat_head(180, 105, 'smile')}
    </g>
    '''
    return svg_wrap(content)

def make_heat_ultimate():
    content = f'''
    <g id="heat-ultimate">
      <!-- 精準火候: Precision flame target lock & roaring wok inferno -->
      <!-- Flame halo -->
      <g filter="url(#glow-fire)">
        <circle cx="180" cy="240" r="145" fill="none" stroke="#e85d4a" stroke-width="4" stroke-dasharray="16,8" opacity="0.7"/>
        <path d="M60 280 Q80 180 120 140 Q150 200 180 100 Q210 200 240 140 Q280 180 300 280 Z" fill="url(#flame-grad)" opacity="0.6"/>
      </g>
      <!-- Precision Target Reticle -->
      <circle cx="180" cy="280" r="65" fill="none" stroke="#f7d070" stroke-width="3.5" stroke-dasharray="8,6"/>
      <circle cx="180" cy="280" r="30" fill="none" stroke="#ffffff" stroke-width="2"/>
      <line x1="180" y1="200" x2="180" y2="360" stroke="#f7d070" stroke-width="2.5"/>
      <line x1="100" y1="280" x2="260" y2="280" stroke="#f7d070" stroke-width="2.5"/>
      <!-- Doctor in centered power stance -->
      {speed_legs(140, 220, 360, 460)}
      {heat_coat_body(180, 235)}
      <!-- Dual wok flames wielded powerfully -->
      <path d="M132 175 Q75 190 85 260 L108 265 Q105 205 148 185 Z" fill="#f8fbff"/>
      <circle cx="88" cy="264" r="9" fill="#d8a77a"/>
      <ellipse cx="70" cy="275" rx="35" ry="24" fill="url(#flame-grad)"/>
      <path d="M228 175 Q285 190 275 260 L252 265 Q255 205 212 185 Z" fill="#f8fbff"/>
      <circle cx="272" cy="264" r="9" fill="#d8a77a"/>
      <ellipse cx="290" cy="275" rx="35" ry="24" fill="url(#flame-grad)"/>
      {heat_head(180, 105, 'focus')}
      <!-- Kanji badge: 精準火候 -->
      <rect x="90" y="420" width="180" height="38" rx="19" fill="#102a43" stroke="#e85d4a" stroke-width="3"/>
      <text x="180" y="445" font-family="sans-serif" font-size="20" font-weight="900" fill="#f38b4a" text-anchor="middle" letter-spacing="4">🔥 精準火候 🔥</text>
    </g>
    '''
    return svg_wrap(content)

# -------------------------------------------------------------
# DR. STRATEGY (處方醫師)
# Palette: Skin #e6b88a, Hair #18314f, Coat #f8fbff, Scrubs #57b2a4, Mint mask #72bdae, Pants #102a43
# Round glasses, clipboard, prescription pen, calming green Rx motif
# -------------------------------------------------------------

def strategy_head(cx=180, cy=110, expr='calm'):
    mouth = f'<path d="M{cx-12} {cy+28} Q{cx} {cy+33} {cx+12} {cy+28}" fill="none" stroke="#7a4b3f" stroke-width="3" stroke-linecap="round"/>'
    if expr == 'smile':
        mouth = f'<path d="M{cx-14} {cy+26} Q{cx} {cy+36} {cx+14} {cy+26}" fill="none" stroke="#7a4b3f" stroke-width="3.5" stroke-linecap="round"/>'
    
    return f'''
    <!-- Head & Hair -->
    <circle cx="{cx}" cy="{cy}" r="46" fill="#e6b88a"/>
    <!-- Neat intellectual side-parted hair -->
    <path d="M{cx-46} {cy-6} Q{cx-36} {cy-52} {cx} {cy-48} Q{cx+44} {cy-48} {cx+46} {cy-2} Q{cx+20} {cy-20} {cx} {cy-20} Q{cx-24} {cy-22} {cx-46} {cy-6} Z" fill="#18314f"/>
    <!-- Eyes -->
    <circle cx="{cx-17}" cy="{cy+2}" r="4" fill="#102a43"/>
    <circle cx="{cx+17}" cy="{cy+2}" r="4" fill="#102a43"/>
    <!-- Round wireframe glasses -->
    <g fill="none" stroke="#26394c" stroke-width="3.5">
      <circle cx="{cx-20}" cy="{cy}" r="15"/>
      <circle cx="{cx+20}" cy="{cy}" r="15"/>
      <path d="M{cx-5} {cy} H{cx+5}"/>
    </g>
    <!-- Eyebrows -->
    <path d="M{cx-30} {cy-18} Q{cx-20} {cy-22} {cx-10} {cy-18}" fill="none" stroke="#18314f" stroke-width="3" stroke-linecap="round"/>
    <path d="M{cx+10} {cy-18} Q{cx+20} {cy-22} {cx+30} {cy-18}" fill="none" stroke="#18314f" stroke-width="3" stroke-linecap="round"/>
    <!-- Mask resting below chin or covering mouth -->
    <path d="M{cx-26} {cy+22} Q{cx} {cy+38} {cx+26} {cy+22} L{cx+20} {cy+45} Q{cx} {cy+52} {cx-20} {cy+45} Z" fill="#72bdae" opacity="0.85"/>
    {mouth}
    '''

def strategy_coat_body(cx=180, cy=240):
    return f'''
    <!-- Torso: Lab coat over mint-green scrubs -->
    <path d="M{cx-48} {cy-80} L{cx-54} {cy+120} H{cx+54} L{cx+48} {cy-80} Z" fill="#f8fbff" stroke="#d9e2ec" stroke-width="2"/>
    <path d="M{cx-24} {cy-80} L{cx} {cy-35} L{cx+24} {cy-80} Z" fill="#57b2a4"/>
    <!-- Stethoscope around neck -->
    <path d="M{cx-35} {cy-75} Q{cx-30} {cy} {cx-15} {cy+25} L{cx-5} {cy+40}" fill="none" stroke="#26394c" stroke-width="4" stroke-linecap="round"/>
    <path d="M{cx+35} {cy-75} Q{cx+30} {cy} {cx+15} {cy+25} L{cx-5} {cy+40}" fill="none" stroke="#26394c" stroke-width="4" stroke-linecap="round"/>
    <circle cx="{cx-5}" cy="{cy+44}" r="8" fill="#a0aec0" stroke="#26394c" stroke-width="2"/>
    <!-- Coat lapels -->
    <path d="M{cx-48} {cy-80} L{cx-18} {cy-15} L{cx-36} {cy+45} L{cx-48} {cy+120}" fill="none" stroke="#cfd8dc" stroke-width="2.5"/>
    <path d="M{cx+48} {cy-80} L{cx+18} {cy-15} L{cx+36} {cy+45} L{cx+48} {cy+120}" fill="none" stroke="#cfd8dc" stroke-width="2.5"/>
    '''

# ----------------- Dr Strategy States -----------------

def make_strategy_idle():
    content = f'''
    <g id="strategy-idle">
      {speed_legs(150, 210, 360, 460)}
      {strategy_coat_body()}
      <!-- Left arm holding clinical order clipboard -->
      <path d="M132 175 Q95 215 105 270 L130 275 Q120 230 152 190 Z" fill="#f8fbff"/>
      <circle cx="112" cy="278" r="9" fill="#e6b88a"/>
      <!-- Clipboard with Rx chart -->
      <rect x="75" y="240" width="55" height="75" rx="5" fill="#8d6e63" stroke="#5d4037" stroke-width="2"/>
      <rect x="80" y="248" width="45" height="62" rx="2" fill="#ffffff"/>
      <rect x="95" y="236" width="16" height="8" rx="2" fill="#cfd8dc"/>
      <path d="M85 260 H115 M85 270 H115 M85 280 H105 M85 290 H110" stroke="#57b2a4" stroke-width="2" stroke-linecap="round"/>
      <!-- Right hand holding fountain pen -->
      <path d="M228 175 Q265 215 250 265 L228 268 Q240 225 210 190 Z" fill="#f8fbff"/>
      <circle cx="244" cy="272" r="9" fill="#e6b88a"/>
      <rect x="242" y="250" width="6" height="26" rx="2" fill="#26394c"/>
      <polygon points="245,244 242,250 248,250" fill="#f3b84a"/>
      {strategy_head(180, 110, 'calm')}
    </g>
    '''
    return svg_wrap(content)

def make_strategy_entrance():
    content = f'''
    <g id="strategy-entrance">
      <!-- Order slips floating in analytical rhythm -->
      <g opacity="0.8">
        <rect x="50" y="140" width="34" height="46" rx="3" fill="#ffffff" stroke="#57b2a4" stroke-width="1.5" transform="rotate(-15 67 163)"/>
        <text x="60" y="165" font-size="12" font-weight="bold" fill="#57b2a4">Rx</text>
        <rect x="280" y="150" width="34" height="46" rx="3" fill="#ffffff" stroke="#57b2a4" stroke-width="1.5" transform="rotate(18 297 173)"/>
        <text x="290" y="175" font-size="12" font-weight="bold" fill="#57b2a4">Rx</text>
      </g>
      {speed_legs(150, 210, 360, 460)}
      {strategy_coat_body(180, 235)}
      <!-- Left arm holding clipboard firmly -->
      <path d="M132 175 Q85 200 95 250 L120 255 Q115 215 152 185 Z" fill="#f8fbff"/>
      <circle cx="102" cy="256" r="9" fill="#e6b88a"/>
      <rect x="70" y="220" width="55" height="75" rx="5" fill="#8d6e63"/>
      <rect x="75" y="228" width="45" height="62" rx="2" fill="#ffffff"/>
      <!-- Right hand gracefully adjusting glasses -->
      <path d="M228 175 Q265 180 235 125 L215 132 Q235 180 208 185 Z" fill="#f8fbff"/>
      <circle cx="228" cy="122" r="8" fill="#e6b88a"/>
      {strategy_head(180, 105, 'smile')}
    </g>
    '''
    return svg_wrap(content)

def make_strategy_prep():
    content = f'''
    <g id="strategy-prep">
      <!-- Methodical checklist prep table -->
      <rect x="50" y="320" width="260" height="38" rx="8" fill="#e2d4be" stroke="#bfa98b" stroke-width="2.5"/>
      <rect x="70" y="328" width="60" height="22" rx="3" fill="#ffffff"/>
      <circle cx="80" cy="339" r="4" fill="#38a169"/>
      <line x1="90" y1="339" x2="120" y2="339" stroke="#718096" stroke-width="2"/>
      <circle cx="150" cy="336" r="10" fill="#48bb78"/>
      <circle cx="180" cy="336" r="10" fill="#e53e3e"/>
      <circle cx="210" cy="336" r="12" fill="#fff" stroke="#cbd5e0"/>
      {speed_legs(155, 205, 355, 460)}
      {strategy_coat_body(180, 235)}
      <!-- Left hand checking off item on pad -->
      <path d="M135 175 Q115 235 125 295 L145 292 Q135 240 155 190 Z" fill="#f8fbff"/>
      <circle cx="132" cy="302" r="9" fill="#e6b88a"/>
      <rect x="110" y="260" width="44" height="58" rx="4" fill="#ffffff" stroke="#57b2a4" stroke-width="2"/>
      <!-- Right hand with prescription pen ticking checkbox -->
      <path d="M225 175 Q245 230 190 280 L180 268 Q220 225 205 190 Z" fill="#f8fbff"/>
      <circle cx="186" cy="278" r="8" fill="#e6b88a"/>
      <line x1="184" y1="280" x2="160" y2="295" stroke="#26394c" stroke-width="3" stroke-linecap="round"/>
      {strategy_head(180, 110, 'calm')}
    </g>
    '''
    return svg_wrap(content)

def make_strategy_cut():
    content = f'''
    <g id="strategy-cut">
      <!-- Timed, calculated cut with stopwatch / metronome precision -->
      <rect x="50" y="320" width="260" height="38" rx="8" fill="#e2d4be" stroke="#bfa98b" stroke-width="2.5"/>
      <rect x="125" y="312" width="50" height="24" rx="3" fill="#ffffff" stroke="#cbd5e0" stroke-width="2"/>
      {speed_legs(155, 205, 355, 460)}
      {strategy_coat_body(180, 235)}
      <!-- Left hand checking wristwatch -->
      <path d="M135 175 Q95 215 120 260 L140 252 Q120 220 155 190 Z" fill="#f8fbff"/>
      <circle cx="125" cy="265" r="9" fill="#e6b88a"/>
      <circle cx="118" cy="260" r="8" fill="#26394c"/>
      <circle cx="118" cy="260" r="6" fill="#f7fafc"/>
      <!-- Right hand timed clean knife cut -->
      <path d="M225 175 Q250 220 215 275 L195 270 Q225 220 205 190 Z" fill="#f8fbff"/>
      <circle cx="212" cy="282" r="9" fill="#e6b88a"/>
      <rect x="206" y="275" width="10" height="42" rx="2" fill="url(#knife-blade)" stroke="#9fb3c8" stroke-width="1.5"/>
      {strategy_head(180, 110, 'calm')}
    </g>
    '''
    return svg_wrap(content)

def make_strategy_cook():
    content = f'''
    <g id="strategy-cook">
      <!-- Calculated wok temperature control with subtle heat waves -->
      <ellipse cx="180" cy="330" rx="88" ry="32" fill="url(#wok-grad)"/>
      <ellipse cx="180" cy="328" rx="80" ry="26" fill="#2d3748"/>
      <ellipse cx="180" cy="328" rx="70" ry="20" fill="#c53030"/>
      <rect x="155" y="322" width="12" height="10" rx="2" fill="#fff"/>
      <rect x="175" y="324" width="12" height="10" rx="2" fill="#fff"/>
      <circle cx="168" cy="326" r="3" fill="#48bb78"/>
      <!-- Gentle calculated steam and temperature gauge -->
      <path d="M150 310 Q145 285 155 260" stroke="#72bdae" stroke-width="2.5" stroke-linecap="round" fill="none" opacity="0.8"/>
      <path d="M210 310 Q215 285 205 260" stroke="#72bdae" stroke-width="2.5" stroke-linecap="round" fill="none" opacity="0.8"/>
      {speed_legs(150, 210, 360, 460)}
      {strategy_coat_body(180, 235)}
      <!-- Left hand holding wok steady -->
      <path d="M132 175 Q90 225 105 295 L125 300 Q115 235 152 185 Z" fill="#f8fbff"/>
      <circle cx="106" cy="300" r="9" fill="#e6b88a"/>
      <!-- Right hand methodically stirring sauce with wooden spoon -->
      <path d="M228 175 Q265 220 230 285 L210 278 Q235 225 208 185 Z" fill="#f8fbff"/>
      <circle cx="226" cy="290" r="9" fill="#e6b88a"/>
      <line x1="226" y1="290" x2="190" y2="330" stroke="#8d6e63" stroke-width="5" stroke-linecap="round"/>
      {strategy_head(180, 105, 'calm')}
    </g>
    '''
    return svg_wrap(content)

def make_strategy_serve():
    content = f'''
    <g id="strategy-serve">
      <!-- Serving with prescription slip: Rx MAPO TOFU -->
      {speed_legs(155, 205, 360, 460)}
      {strategy_coat_body(180, 235)}
      <!-- Left hand presenting delicious bowl -->
      <path d="M135 175 Q115 230 145 285 L165 280 Q140 230 155 185 Z" fill="#f8fbff"/>
      <circle cx="148" cy="290" r="9" fill="#e6b88a"/>
      <ellipse cx="165" cy="290" rx="42" ry="16" fill="#2d3748" stroke="#57b2a4" stroke-width="2"/>
      <ellipse cx="165" cy="287" rx="34" ry="11" fill="#c53030"/>
      <rect x="150" y="283" width="9" height="8" rx="2" fill="#ffffff"/>
      <rect x="165" y="284" width="9" height="8" rx="2" fill="#ffffff"/>
      <circle cx="158" cy="286" r="3" fill="#48bb78"/>
      <!-- Right hand holding stamped prescription ticket -->
      <path d="M225 175 Q260 215 245 270 L225 272 Q235 225 205 185 Z" fill="#f8fbff"/>
      <circle cx="242" cy="275" r="9" fill="#e6b88a"/>
      <rect x="228" y="240" width="46" height="60" rx="3" fill="#ffffff" stroke="#57b2a4" stroke-width="2"/>
      <text x="251" y="258" font-family="sans-serif" font-size="12" font-weight="bold" fill="#57b2a4" text-anchor="middle">Rx 處方</text>
      <rect x="235" y="266" width="32" height="14" rx="2" fill="#e6fffa" stroke="#38b2ac"/>
      <text x="251" y="277" font-family="sans-serif" font-size="9" font-weight="bold" fill="#234e52" text-anchor="middle">COMPLETE</text>
      {strategy_head(180, 105, 'smile')}
    </g>
    '''
    return svg_wrap(content)

def make_strategy_ultimate():
    content = f'''
    <g id="strategy-ultimate">
      <!-- Craving 處方: Glowing prescription seal, soothing mint green aura waves, calming leaves -->
      <g filter="url(#glow-green)">
        <!-- Soothing concentric ripple circles -->
        <circle cx="180" cy="240" r="145" fill="none" stroke="#57b2a4" stroke-width="4" opacity="0.6"/>
        <circle cx="180" cy="240" r="115" fill="none" stroke="#8ac6a7" stroke-width="3" stroke-dasharray="12,8" opacity="0.7"/>
        <circle cx="180" cy="240" r="85" fill="none" stroke="#b2f5ea" stroke-width="2.5" opacity="0.8"/>
      </g>
      <!-- Calming herbal leaves drifting -->
      <path d="M70 160 Q85 140 100 155 Q85 170 70 160 Z" fill="#57b2a4" opacity="0.8"/>
      <path d="M280 170 Q295 150 310 165 Q295 180 280 170 Z" fill="#57b2a4" opacity="0.8"/>
      <path d="M90 320 Q105 300 120 315 Q105 330 90 320 Z" fill="#8ac6a7" opacity="0.8"/>
      <path d="M260 310 Q275 290 290 305 Q275 320 260 310 Z" fill="#8ac6a7" opacity="0.8"/>
      <!-- Doctor holding giant glowing prescription seal -->
      {speed_legs(150, 210, 360, 460)}
      {strategy_coat_body(180, 235)}
      <!-- Arms holding up glowing clinical Rx seal -->
      <path d="M135 175 Q110 210 135 255 L155 250 Q135 210 155 185 Z" fill="#f8fbff"/>
      <circle cx="138" cy="258" r="9" fill="#e6b88a"/>
      <path d="M225 175 Q250 210 225 255 L205 250 Q225 210 205 185 Z" fill="#f8fbff"/>
      <circle cx="222" cy="258" r="9" fill="#e6b88a"/>
      <!-- Glowing Rx Prescription Seal -->
      <rect x="125" y="215" width="110" height="110" rx="18" fill="url(#rx-grad)" stroke="#ffffff" stroke-width="4" filter="url(#glow-green)"/>
      <text x="180" y="260" font-family="serif" font-size="42" font-weight="900" fill="#ffffff" text-anchor="middle">Rx</text>
      <text x="180" y="285" font-family="sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle" letter-spacing="2">CRAVING 處方</text>
      <text x="180" y="306" font-family="sans-serif" font-size="11" fill="#e6fffa" text-anchor="middle">-18% CRAVING</text>
      {strategy_head(180, 105, 'smile')}
      <!-- Kanji badge: Craving 處方 -->
      <rect x="90" y="420" width="180" height="38" rx="19" fill="#102a43" stroke="#57b2a4" stroke-width="3"/>
      <text x="180" y="445" font-family="sans-serif" font-size="20" font-weight="900" fill="#8ac6a7" text-anchor="middle" letter-spacing="4">📋 Craving 處方 📋</text>
    </g>
    '''
    return svg_wrap(content)

# ----------------- Write Files -----------------

doctors_data = {
    'doctor_speed': {
        'entrance': make_speed_entrance(),
        'idle': make_speed_idle(),
        'prep': make_speed_prep(),
        'cut': make_speed_cut(),
        'cook': make_speed_cook(),
        'serve': make_speed_serve(),
        'ultimate': make_speed_ultimate(),
    },
    'doctor_heat': {
        'entrance': make_heat_entrance(),
        'idle': make_heat_idle(),
        'prep': make_heat_prep(),
        'cut': make_heat_cut(),
        'cook': make_heat_cook(),
        'serve': make_heat_serve(),
        'ultimate': make_heat_ultimate(),
    },
    'doctor_strategy': {
        'entrance': make_strategy_entrance(),
        'idle': make_strategy_idle(),
        'prep': make_strategy_prep(),
        'cut': make_strategy_cut(),
        'cook': make_strategy_cook(),
        'serve': make_strategy_serve(),
        'ultimate': make_strategy_ultimate(),
    }
}

count = 0
for doc_id, states in doctors_data.items():
    for state_name, svg_content in states.items():
        fname = f"{doc_id}_{state_name}.svg"
        fpath = OUT_DIR / fname
        fpath.write_text(svg_content.strip(), encoding='utf-8')
        count += 1
        print(f"Wrote {fname}")

print(f"Total doctor assets generated: {count}")
