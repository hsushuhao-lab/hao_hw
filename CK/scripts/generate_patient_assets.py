from pathlib import Path

OUT_DIR = Path(__file__).resolve().parents[1] / 'assets' / 'characters' / 'patients'
OUT_DIR.mkdir(parents=True, exist_ok=True)

def svg_wrap(content):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 440" width="320" height="440">
  <defs>
    <filter id="pat-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <linearGradient id="bowl-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
    <linearGradient id="tofu-red" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#e53e3e"/>
      <stop offset="100%" stop-color="#9b2c2c"/>
    </linearGradient>
  </defs>
{content}
</svg>'''

# -------------------------------------------------------------
# Common props: Mapo Tofu Bowl for 'eat' state
# -------------------------------------------------------------
def mapo_bowl(bx=160, by=250):
    return f'''
    <!-- Steaming Bowl of Mapo Tofu -->
    <ellipse cx="{bx}" cy="{by+12}" rx="38" ry="14" fill="url(#bowl-grad)" stroke="#cbd5e0" stroke-width="2"/>
    <ellipse cx="{bx}" cy="{by+10}" rx="32" ry="10" fill="url(#tofu-red)"/>
    <rect x="{bx-14}" y="{by+6}" width="7" height="6" rx="1.5" fill="#ffffff"/>
    <rect x="{bx-2}" y="{by+7}" width="7" height="6" rx="1.5" fill="#ffffff"/>
    <rect x="{bx+10}" y="{by+5}" width="7" height="6" rx="1.5" fill="#ffffff"/>
    <circle cx="{bx-7}" cy="{by+8}" r="2.5" fill="#48bb78"/>
    <circle cx="{bx+6}" cy="{by+8}" r="2.5" fill="#48bb78"/>
    <!-- Steam -->
    <path d="M{bx-12} {by} Q{bx-16} {by-18} {bx-8} {by-32}" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" fill="none" opacity="0.8"/>
    <path d="M{bx+10} {by} Q{bx+15} {by-18} {bx+6} {by-32}" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" fill="none" opacity="0.8"/>
    '''

def clinic_chair(cx=160, cy=280):
    return f'''
    <!-- Clinic Consultation Chair -->
    <rect x="{cx-45}" y="{cy}" width="90" height="12" rx="5" fill="#718096" stroke="#4a5568" stroke-width="1.5"/>
    <rect x="{cx-38}" y="{cy-55}" width="76" height="58" rx="8" fill="#4a5568" stroke="#2d3748" stroke-width="2"/>
    <!-- Chair stem & caster base -->
    <rect x="{cx-6}" y="{cy+12}" width="12" height="50" rx="3" fill="#a0aec0"/>
    <path d="M{cx-40} {cy+62} L{cx+40} {cy+62}" stroke="#2d3748" stroke-width="5" stroke-linecap="round"/>
    <circle cx="{cx-36}" cy="{cy+66}" r="5" fill="#1a202c"/>
    <circle cx="{cx+36}" cy="{cy+66}" r="5" fill="#1a202c"/>
    '''

# -------------------------------------------------------------
# 1. OFFICE WORKER (焦慮上班族)
# Suit #2d3748, red tie #e53e3e, briefcase, nervous watch glance
# -------------------------------------------------------------
def office_head(cx=160, cy=105, expr='nervous'):
    mouth = f'<path d="M{cx-10} {cy+28} Q{cx} {cy+22} {cx+10} {cy+28}" stroke="#742a2a" stroke-width="2.5" fill="none"/>'
    sweat = f'<path d="M{cx+32} {cy+5} Q{cx+38} {cy+15} {cx+34} {cy+20} Q{cx+30} {cy+15} {cx+32} {cy+5} Z" fill="#63b3ed"/>'
    if expr == 'eat':
        mouth = f'<ellipse cx="{cx}" cy="{cy+28}" rx="8" ry="7" fill="#742a2a"/><ellipse cx="{cx}" cy="{cy+30}" rx="5" ry="3" fill="#fc8181"/>'
        sweat = ''
    elif expr == 'leave':
        mouth = f'<path d="M{cx-10} {cy+25} Q{cx} {cy+35} {cx+10} {cy+25}" stroke="#742a2a" stroke-width="3" fill="none"/>'
        sweat = ''
    
    return f'''
    <!-- Head & Anxious office hair -->
    <circle cx="{cx}" cy="{cy}" r="40" fill="#e6b88a"/>
    <path d="M{cx-40} {cy-5} Q{cx-36} {cy-46} {cx} {cy-44} Q{cx+40} {cy-44} {cx+42} {cy-4} Q{cx+20} {cy-20} {cx} {cy-20} Q{cx-22} {cy-20} {cx-40} {cy-5} Z" fill="#2d3748"/>
    <!-- Worried angled eyebrows -->
    <path d="M{cx-26} {cy-14} L{cx-8} {cy-18}" stroke="#1a202c" stroke-width="3" stroke-linecap="round"/>
    <path d="M{cx+8} {cy-18} L{cx+26} {cy-14}" stroke="#1a202c" stroke-width="3" stroke-linecap="round"/>
    <!-- Eyes -->
    <circle cx="{cx-15}" cy="{cy}" r="3.5" fill="#1a202c"/>
    <circle cx="{cx+15}" cy="{cy}" r="3.5" fill="#1a202c"/>
    {mouth}
    {sweat}
    '''

def make_office_walk_in():
    content = f'''
    <g id="office-walk-in">
      <!-- Legs walking briskly -->
      <path d="M145 290 L125 390 L115 390" stroke="#1a202c" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M175 290 L195 385 L215 390" stroke="#1a202c" stroke-width="18" stroke-linecap="round" stroke-linejoin="round"/>
      <!-- Suit jacket & red tie -->
      <path d="M125 145 L115 295 H205 L195 145 Z" fill="#2d3748"/>
      <polygon points="152,145 168,145 165,225 160,235 155,225" fill="#e53e3e"/>
      <!-- Left arm with briefcase -->
      <path d="M125 150 L95 240 L85 240" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <circle cx="85" cy="245" r="7" fill="#e6b88a"/>
      <rect x="65" y="240" width="30" height="38" rx="4" fill="#744210" stroke="#975a16" stroke-width="1.5"/>
      <!-- Right arm swinging check wristwatch -->
      <path d="M195 150 L225 210 L190 230" stroke="#2d3748" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="190" cy="230" r="7" fill="#e6b88a"/>
      <circle cx="205" cy="225" r="5" fill="#f6ad55"/>
      {office_head(160, 105, 'nervous')}
    </g>
    '''
    return svg_wrap(content)

def make_office_sit():
    content = f'''
    <g id="office-sit">
      {clinic_chair(160, 270)}
      <!-- Seated legs -->
      <path d="M135 270 L130 350 L120 375" stroke="#1a202c" stroke-width="16" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#1a202c" stroke-width="16" stroke-linecap="round"/>
      <!-- Torso -->
      <path d="M125 145 L120 275 H200 L195 145 Z" fill="#2d3748"/>
      <polygon points="152,145 168,145 165,225 160,235 155,225" fill="#e53e3e"/>
      <!-- Hands resting nervously on knees -->
      <path d="M125 150 L105 220 L130 260" stroke="#2d3748" stroke-width="14" stroke-linecap="round"/>
      <circle cx="132" cy="265" r="7" fill="#e6b88a"/>
      <path d="M195 150 L215 220 L190 260" stroke="#2d3748" stroke-width="14" stroke-linecap="round"/>
      <circle cx="188" cy="265" r="7" fill="#e6b88a"/>
      <!-- Briefcase on floor next to chair -->
      <rect x="75" y="325" width="28" height="36" rx="4" fill="#744210" stroke="#975a16" stroke-width="1.5"/>
      {office_head(160, 105, 'nervous')}
    </g>
    '''
    return svg_wrap(content)

def make_office_order():
    content = f'''
    <g id="office-order">
      {clinic_chair(160, 270)}
      <!-- Seated legs -->
      <path d="M135 270 L130 350 L120 375" stroke="#1a202c" stroke-width="16" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#1a202c" stroke-width="16" stroke-linecap="round"/>
      <!-- Torso leaning forward eagerly -->
      <path d="M125 145 L120 275 H200 L195 145 Z" fill="#2d3748"/>
      <polygon points="152,145 168,145 165,225 160,235 155,225" fill="#e53e3e"/>
      <!-- Urgent hands gesturing craving time! -->
      <path d="M125 150 L95 190 L85 170" stroke="#2d3748" stroke-width="14" stroke-linecap="round"/>
      <circle cx="85" cy="168" r="7" fill="#e6b88a"/>
      <!-- Right hand tapping wristwatch -->
      <path d="M195 150 L215 190 L180 185" stroke="#2d3748" stroke-width="14" stroke-linecap="round"/>
      <circle cx="178" cy="185" r="7" fill="#e6b88a"/>
      <!-- Speech balloon: 20 min left! -->
      <rect x="180" y="30" width="125" height="42" rx="12" fill="#ffffff" stroke="#e53e3e" stroke-width="2"/>
      <text x="242" y="56" font-family="sans-serif" font-size="12" font-weight="bold" fill="#c53030" text-anchor="middle">二十分鐘內！</text>
      <polygon points="195,72 205,72 190,85" fill="#ffffff" stroke="#e53e3e" stroke-width="1.5"/>
      {office_head(160, 105, 'nervous')}
    </g>
    '''
    return svg_wrap(content)

def make_office_eat():
    content = f'''
    <g id="office-eat">
      {clinic_chair(160, 270)}
      <!-- Seated legs -->
      <path d="M135 270 L130 350 L120 375" stroke="#1a202c" stroke-width="16" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#1a202c" stroke-width="16" stroke-linecap="round"/>
      <!-- Torso -->
      <path d="M125 145 L120 275 H200 L195 145 Z" fill="#2d3748"/>
      <!-- Arms holding bowl and spoon eating rapidly! -->
      <path d="M125 150 L115 220 L145 250" stroke="#2d3748" stroke-width="14" stroke-linecap="round"/>
      <circle cx="145" cy="252" r="7" fill="#e6b88a"/>
      <path d="M195 150 L205 210 L175 230" stroke="#2d3748" stroke-width="14" stroke-linecap="round"/>
      <circle cx="172" cy="230" r="7" fill="#e6b88a"/>
      <line x1="172" y1="230" x2="160" y2="155" stroke="#a0aec0" stroke-width="3" stroke-linecap="round"/>
      {mapo_bowl(160, 240)}
      {office_head(160, 105, 'eat')}
    </g>
    '''
    return svg_wrap(content)

def make_office_leave():
    content = f'''
    <g id="office-leave">
      <!-- Walking out calmly, briefcase in hand, craving satisfied! -->
      <path d="M145 290 L170 390 L185 390" stroke="#1a202c" stroke-width="18" stroke-linecap="round"/>
      <path d="M175 290 L135 385 L125 385" stroke="#1a202c" stroke-width="18" stroke-linecap="round"/>
      <path d="M125 145 L115 295 H205 L195 145 Z" fill="#2d3748"/>
      <polygon points="152,145 168,145 165,225 160,235 155,225" fill="#e53e3e"/>
      <!-- Left arm with briefcase -->
      <path d="M125 150 L100 230 L95 230" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <circle cx="95" cy="235" r="7" fill="#e6b88a"/>
      <rect x="75" y="230" width="30" height="38" rx="4" fill="#744210" stroke="#975a16" stroke-width="1.5"/>
      <!-- Right hand waving thank you -->
      <path d="M195 150 L230 180 L235 145" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <circle cx="235" cy="142" r="8" fill="#e6b88a"/>
      {office_head(160, 105, 'leave')}
    </g>
    '''
    return svg_wrap(content)

# -------------------------------------------------------------
# 2. STUDENT (熬夜學生)
# Hoodie #4a5568, backpack straps, glasses, tired studious stance
# -------------------------------------------------------------
def student_head(cx=160, cy=105, expr='tired'):
    mouth = f'<path d="M{cx-10} {cy+28} H{cx+10}" stroke="#742a2a" stroke-width="2.5" stroke-linecap="round"/>'
    if expr == 'eat':
        mouth = f'<ellipse cx="{cx}" cy="{cy+28}" rx="8" ry="7" fill="#742a2a"/>'
    elif expr == 'smile':
        mouth = f'<path d="M{cx-10} {cy+25} Q{cx} {cy+35} {cx+10} {cy+25}" stroke="#742a2a" stroke-width="3" fill="none"/>'
    
    return f'''
    <!-- Head & Shaggy student hair -->
    <circle cx="{cx}" cy="{cy}" r="40" fill="#e6b88a"/>
    <path d="M{cx-42} {cy} Q{cx-40} {cy-48} {cx} {cy-46} Q{cx+40} {cy-48} {cx+42} {cy} Q{cx+15} {cy-15} {cx-10} {cy-15} Q{cx-30} {cy-12} {cx-42} {cy} Z" fill="#2d3748"/>
    <!-- Weary student round glasses -->
    <g fill="none" stroke="#4a5568" stroke-width="2.5">
      <circle cx="{cx-16}" cy="{cy+2}" r="12"/>
      <circle cx="{cx+16}" cy="{cy+2}" r="12"/>
      <line x1="{cx-4}" y1="{cy+2}" x2="{cx+4}" y2="{cy+2}"/>
    </g>
    <circle cx="{cx-16}" cy="{cy+2}" r="3" fill="#1a202c"/>
    <circle cx="{cx+16}" cy="{cy+2}" r="3" fill="#1a202c"/>
    <!-- Droopy tired eyebrows -->
    <path d="M{cx-24} {cy-14} Q{cx-15} {cy-12} {cx-8} {cy-16}" stroke="#2d3748" stroke-width="2.5" fill="none"/>
    <path d="M{cx+8} {cy-16} Q{cx+15} {cy-12} {cx+24} {cy-14}" stroke="#2d3748" stroke-width="2.5" fill="none"/>
    {mouth}
    '''

def make_student_walk_in():
    content = f'''
    <g id="student-walk-in">
      <path d="M145 290 L130 385 L120 385" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M175 290 L190 380 L205 380" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <!-- Cozy student hoodie -->
      <path d="M120 145 L110 295 H210 L200 145 Z" fill="#4a5568" rx="8"/>
      <!-- Backpack straps -->
      <rect x="130" y="145" width="12" height="150" fill="#2d3748" rx="4"/>
      <rect x="178" y="145" width="12" height="150" fill="#2d3748" rx="4"/>
      <!-- Arms holding backpack straps -->
      <path d="M120 150 L105 220 L132 230" stroke="#4a5568" stroke-width="14" stroke-linecap="round"/>
      <circle cx="134" cy="230" r="7" fill="#e6b88a"/>
      <path d="M200 150 L215 220 L188 230" stroke="#4a5568" stroke-width="14" stroke-linecap="round"/>
      <circle cx="186" cy="230" r="7" fill="#e6b88a"/>
      {student_head(160, 105, 'tired')}
    </g>
    '''
    return svg_wrap(content)

def make_student_sit():
    content = f'''
    <g id="student-sit">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M120 145 L115 275 H205 L200 145 Z" fill="#4a5568"/>
      <!-- Backpack resting on back of chair -->
      <rect x="195" y="200" width="35" height="60" rx="8" fill="#1a202c"/>
      <!-- Hands resting wearily on lap -->
      <path d="M120 150 L105 220 L140 260" stroke="#4a5568" stroke-width="14" stroke-linecap="round"/>
      <circle cx="142" cy="262" r="7" fill="#e6b88a"/>
      <path d="M200 150 L215 220 L180 260" stroke="#4a5568" stroke-width="14" stroke-linecap="round"/>
      <circle cx="178" cy="262" r="7" fill="#e6b88a"/>
      {student_head(160, 105, 'tired')}
    </g>
    '''
    return svg_wrap(content)

def make_student_order():
    content = f'''
    <g id="student-order">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M120 145 L115 275 H205 L200 145 Z" fill="#4a5568"/>
      <!-- Hand raising asking for: no scallions please! -->
      <path d="M120 150 L105 210 L135 230" stroke="#4a5568" stroke-width="14" stroke-linecap="round"/>
      <circle cx="138" cy="232" r="7" fill="#e6b88a"/>
      <path d="M200 150 L220 180 L215 150" stroke="#4a5568" stroke-width="14" stroke-linecap="round"/>
      <circle cx="215" cy="146" r="7" fill="#e6b88a"/>
      <!-- Speech bubble: 不要蔥 -->
      <rect x="175" y="30" width="135" height="42" rx="12" fill="#ffffff" stroke="#4a5568" stroke-width="2"/>
      <text x="242" y="56" font-family="sans-serif" font-size="12" font-weight="bold" fill="#2d3748" text-anchor="middle">小辣 · 不要蔥！</text>
      <polygon points="190,72 200,72 185,85" fill="#ffffff" stroke="#4a5568" stroke-width="1.5"/>
      {student_head(160, 105, 'tired')}
    </g>
    '''
    return svg_wrap(content)

def make_student_eat():
    content = f'''
    <g id="student-eat">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M120 145 L115 275 H205 L200 145 Z" fill="#4a5568"/>
      <path d="M120 150 L115 220 L145 250" stroke="#4a5568" stroke-width="14" stroke-linecap="round"/>
      <circle cx="145" cy="252" r="7" fill="#e6b88a"/>
      <path d="M200 150 L205 210 L175 230" stroke="#4a5568" stroke-width="14" stroke-linecap="round"/>
      <circle cx="172" cy="230" r="7" fill="#e6b88a"/>
      <line x1="172" y1="230" x2="160" y2="155" stroke="#a0aec0" stroke-width="3" stroke-linecap="round"/>
      {mapo_bowl(160, 240)}
      {student_head(160, 105, 'eat')}
    </g>
    '''
    return svg_wrap(content)

def make_student_leave():
    content = f'''
    <g id="student-leave">
      <path d="M145 290 L165 385 L180 385" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M175 290 L135 380 L125 380" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M120 145 L110 295 H210 L200 145 Z" fill="#4a5568"/>
      <!-- Energized student walking out ready to study -->
      <path d="M120 150 L105 210 L125 240" stroke="#4a5568" stroke-width="14" stroke-linecap="round"/>
      <circle cx="128" cy="242" r="7" fill="#e6b88a"/>
      <path d="M200 150 L225 190 L240 160" stroke="#4a5568" stroke-width="14" stroke-linecap="round"/>
      <circle cx="242" cy="156" r="7" fill="#e6b88a"/>
      {student_head(160, 105, 'smile')}
    </g>
    '''
    return svg_wrap(content)

# -------------------------------------------------------------
# 3. DRIVER (長班司機)
# Cap #742a2a, red shirt #c53030, towel around neck, thermos bottle
# -------------------------------------------------------------
def driver_head(cx=160, cy=105, expr='neutral'):
    mouth = f'<path d="M{cx-12} {cy+28} H{cx+12}" stroke="#742a2a" stroke-width="3.5" stroke-linecap="round"/>'
    if expr == 'eat':
        mouth = f'<ellipse cx="{cx}" cy="{cy+28}" rx="9" ry="8" fill="#742a2a"/>'
    elif expr == 'smile':
        mouth = f'<path d="M{cx-12} {cy+25} Q{cx} {cy+36} {cx+12} {cy+25}" stroke="#742a2a" stroke-width="3.5" fill="none"/>'
    
    return f'''
    <!-- Head -->
    <circle cx="{cx}" cy="{cy}" r="42" fill="#d69e2e"/>
    <!-- Driver Cap -->
    <path d="M{cx-44} {cy-12} Q{cx-40} {cy-50} {cx} {cy-48} Q{cx+40} {cy-50} {cx+44} {cy-12} Z" fill="#742a2a"/>
    <path d="M{cx-48} {cy-10} Q{cx} {cy-22} {cx+48} {cy-10} L{cx+55} {cy-5} Q{cx} {cy-16} {cx-55} {cy-5} Z" fill="#4a1a1a"/>
    <!-- Sturdy beard stubble / jaw -->
    <path d="M{cx-25} {cy+35} Q{cx} {cy+45} {cx+25} {cy+35}" stroke="#975a16" stroke-width="3" stroke-dasharray="3,3" fill="none"/>
    <!-- Eyes -->
    <circle cx="{cx-16}" cy="{cy+5}" r="4" fill="#1a202c"/>
    <circle cx="{cx+16}" cy="{cy+5}" r="4" fill="#1a202c"/>
    <!-- Strong eyebrows -->
    <path d="M{cx-26} {cy-6} H{cx-6}" stroke="#4a1a1a" stroke-width="4" stroke-linecap="round"/>
    <path d="M{cx+6} {cy-6} H{cx+26}" stroke="#4a1a1a" stroke-width="4" stroke-linecap="round"/>
    <!-- White towel around neck -->
    <path d="M{cx-35} {cy+30} Q{cx} {cy+55} {cx+35} {cy+30}" stroke="#ffffff" stroke-width="8" stroke-linecap="round" fill="none"/>
    {mouth}
    '''

def make_driver_walk_in():
    content = f'''
    <g id="driver-walk-in">
      <path d="M140 290 L120 385 L110 385" stroke="#2d3748" stroke-width="20" stroke-linecap="round"/>
      <path d="M180 290 L200 380 L215 380" stroke="#2d3748" stroke-width="20" stroke-linecap="round"/>
      <!-- Sturdy polo shirt & vest -->
      <path d="M115 145 L105 295 H215 L205 145 Z" fill="#c53030"/>
      <!-- Left arm holding big thermos bottle -->
      <path d="M115 150 L85 225 L80 240" stroke="#c53030" stroke-width="16" stroke-linecap="round"/>
      <circle cx="80" cy="245" r="8" fill="#d69e2e"/>
      <rect x="68" y="235" width="22" height="45" rx="5" fill="#4a5568" stroke="#718096" stroke-width="2"/>
      <!-- Right arm swinging -->
      <path d="M205 150 L235 220 L220 245" stroke="#c53030" stroke-width="16" stroke-linecap="round"/>
      <circle cx="218" cy="248" r="8" fill="#d69e2e"/>
      {driver_head(160, 105, 'neutral')}
    </g>
    '''
    return svg_wrap(content)

def make_driver_sit():
    content = f'''
    <g id="driver-sit">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#2d3748" stroke-width="18" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#2d3748" stroke-width="18" stroke-linecap="round"/>
      <path d="M115 145 L110 275 H210 L205 145 Z" fill="#c53030"/>
      <!-- Arms resting broadly on knees -->
      <path d="M115 150 L95 220 L130 260" stroke="#c53030" stroke-width="16" stroke-linecap="round"/>
      <circle cx="132" cy="265" r="8" fill="#d69e2e"/>
      <path d="M205 150 L225 220 L190 260" stroke="#c53030" stroke-width="16" stroke-linecap="round"/>
      <circle cx="188" cy="265" r="8" fill="#d69e2e"/>
      <rect x="65" y="320" width="22" height="45" rx="5" fill="#4a5568"/>
      {driver_head(160, 105, 'neutral')}
    </g>
    '''
    return svg_wrap(content)

def make_driver_order():
    content = f'''
    <g id="driver-order">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#2d3748" stroke-width="18" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#2d3748" stroke-width="18" stroke-linecap="round"/>
      <path d="M115 145 L110 275 H210 L205 145 Z" fill="#c53030"/>
      <!-- Hearty gesture: 大辣！飯多！蔥多！ -->
      <path d="M115 150 L95 210 L125 220" stroke="#c53030" stroke-width="16" stroke-linecap="round"/>
      <circle cx="128" cy="222" r="8" fill="#d69e2e"/>
      <path d="M205 150 L235 180 L225 140" stroke="#c53030" stroke-width="16" stroke-linecap="round"/>
      <circle cx="225" cy="138" r="8" fill="#d69e2e"/>
      <!-- Speech bubble -->
      <rect x="175" y="25" width="135" height="42" rx="12" fill="#ffffff" stroke="#c53030" stroke-width="2"/>
      <text x="242" y="51" font-family="sans-serif" font-size="12" font-weight="bold" fill="#c53030" text-anchor="middle">大辣！飯多！</text>
      <polygon points="190,67 200,67 185,80" fill="#ffffff" stroke="#c53030" stroke-width="1.5"/>
      {driver_head(160, 105, 'neutral')}
    </g>
    '''
    return svg_wrap(content)

def make_driver_eat():
    content = f'''
    <g id="driver-eat">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#2d3748" stroke-width="18" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#2d3748" stroke-width="18" stroke-linecap="round"/>
      <path d="M115 145 L110 275 H210 L205 145 Z" fill="#c53030"/>
      <path d="M115 150 L110 220 L145 250" stroke="#c53030" stroke-width="16" stroke-linecap="round"/>
      <circle cx="145" cy="252" r="8" fill="#d69e2e"/>
      <path d="M205 150 L210 210 L175 230" stroke="#c53030" stroke-width="16" stroke-linecap="round"/>
      <circle cx="172" cy="230" r="8" fill="#d69e2e"/>
      <line x1="172" y1="230" x2="160" y2="155" stroke="#a0aec0" stroke-width="3" stroke-linecap="round"/>
      {mapo_bowl(160, 240)}
      {driver_head(160, 105, 'eat')}
    </g>
    '''
    return svg_wrap(content)

def make_driver_leave():
    content = f'''
    <g id="driver-leave">
      <path d="M140 290 L165 385 L180 385" stroke="#2d3748" stroke-width="20" stroke-linecap="round"/>
      <path d="M180 290 L135 380 L125 380" stroke="#2d3748" stroke-width="20" stroke-linecap="round"/>
      <path d="M115 145 L105 295 H215 L205 145 Z" fill="#c53030"/>
      <!-- Thermos in hand, giving thumbs up -->
      <path d="M115 150 L85 220 L80 240" stroke="#c53030" stroke-width="16" stroke-linecap="round"/>
      <circle cx="80" cy="245" r="8" fill="#d69e2e"/>
      <rect x="68" y="235" width="22" height="45" rx="5" fill="#4a5568"/>
      <path d="M205 150 L235 180 L230 150" stroke="#c53030" stroke-width="16" stroke-linecap="round"/>
      <circle cx="230" cy="145" r="8" fill="#d69e2e"/>
      {driver_head(160, 105, 'smile')}
    </g>
    '''
    return svg_wrap(content)

# -------------------------------------------------------------
# 4. AUNTIE (熱情阿姨)
# Floral vest #dd6b20 / #d69e2e, market tote bag, warm smile
# -------------------------------------------------------------
def auntie_head(cx=160, cy=105, expr='warm'):
    mouth = f'<path d="M{cx-14} {cy+24} Q{cx} {cy+36} {cx+14} {cy+24}" stroke="#742a2a" stroke-width="3" fill="none"/>'
    if expr == 'eat':
        mouth = f'<ellipse cx="{cx}" cy="{cy+28}" rx="8" ry="7" fill="#742a2a"/>'
    
    return f'''
    <!-- Head & Auntie perm curls -->
    <circle cx="{cx}" cy="{cy}" r="42" fill="#e6b88a"/>
    <!-- Curls -->
    <circle cx="{cx-36}" cy="{cy-18}" r="14" fill="#5a3a22"/>
    <circle cx="{cx-24}" cy="{cy-38}" r="15" fill="#5a3a22"/>
    <circle cx="{cx}" cy="{cy-44}" r="16" fill="#5a3a22"/>
    <circle cx="{cx+24}" cy="{cy-38}" r="15" fill="#5a3a22"/>
    <circle cx="{cx+36}" cy="{cy-18}" r="14" fill="#5a3a22"/>
    <!-- Cheerful eyes with laugh lines -->
    <path d="M{cx-22} {cy+4} Q{cx-14} {cy-2} {cx-6} {cy+4}" stroke="#1a202c" stroke-width="3" fill="none"/>
    <path d="M{cx+6} {cy+4} Q{cx+14} {cy-2} {cx+22} {cy+4}" stroke="#1a202c" stroke-width="3" fill="none"/>
    <!-- Rosy cheeks -->
    <circle cx="{cx-22}" cy="{cy+16}" r="7" fill="#fed7d7" opacity="0.8"/>
    <circle cx="{cx+22}" cy="{cy+16}" r="7" fill="#fed7d7" opacity="0.8"/>
    {mouth}
    '''

def make_auntie_walk_in():
    content = f'''
    <g id="auntie-walk-in">
      <path d="M140 290 L125 385 L115 385" stroke="#4a5568" stroke-width="16" stroke-linecap="round"/>
      <path d="M180 290 L195 380 L205 380" stroke="#4a5568" stroke-width="16" stroke-linecap="round"/>
      <!-- Colorful auntie cardigan -->
      <path d="M115 145 L105 295 H215 L205 145 Z" fill="#dd6b20"/>
      <circle cx="140" cy="180" r="5" fill="#fbd38d"/>
      <circle cx="180" cy="180" r="5" fill="#fbd38d"/>
      <circle cx="160" cy="220" r="5" fill="#fbd38d"/>
      <!-- Left arm with shopping bag -->
      <path d="M115 150 L85 220 L75 230" stroke="#dd6b20" stroke-width="14" stroke-linecap="round"/>
      <circle cx="75" cy="235" r="7" fill="#e6b88a"/>
      <rect x="55" y="235" width="34" height="42" rx="4" fill="#ed8936" stroke="#c05621" stroke-width="1.5"/>
      <!-- Right hand greeting doctor -->
      <path d="M205 150 L235 190 L240 160" stroke="#dd6b20" stroke-width="14" stroke-linecap="round"/>
      <circle cx="240" cy="155" r="7" fill="#e6b88a"/>
      {auntie_head(160, 105, 'warm')}
    </g>
    '''
    return svg_wrap(content)

def make_auntie_sit():
    content = f'''
    <g id="auntie-sit">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#4a5568" stroke-width="16" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#4a5568" stroke-width="16" stroke-linecap="round"/>
      <path d="M115 145 L110 275 H210 L205 145 Z" fill="#dd6b20"/>
      <!-- Hands resting comfortably on lap -->
      <path d="M115 150 L95 220 L130 260" stroke="#dd6b20" stroke-width="14" stroke-linecap="round"/>
      <circle cx="132" cy="265" r="7" fill="#e6b88a"/>
      <path d="M205 150 L225 220 L190 260" stroke="#dd6b20" stroke-width="14" stroke-linecap="round"/>
      <circle cx="188" cy="265" r="7" fill="#e6b88a"/>
      <!-- Tote bag on floor -->
      <rect x="65" y="325" width="34" height="40" rx="4" fill="#ed8936"/>
      {auntie_head(160, 105, 'warm')}
    </g>
    '''
    return svg_wrap(content)

def make_auntie_order():
    content = f'''
    <g id="auntie-order">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#4a5568" stroke-width="16" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#4a5568" stroke-width="16" stroke-linecap="round"/>
      <path d="M115 145 L110 275 H210 L205 145 Z" fill="#dd6b20"/>
      <!-- Expressive auntie hands: 豆腐多一點！記得吃飯喔！ -->
      <path d="M115 150 L85 190 L95 160" stroke="#dd6b20" stroke-width="14" stroke-linecap="round"/>
      <circle cx="98" cy="156" r="7" fill="#e6b88a"/>
      <path d="M205 150 L235 190 L225 160" stroke="#dd6b20" stroke-width="14" stroke-linecap="round"/>
      <circle cx="222" cy="156" r="7" fill="#e6b88a"/>
      <!-- Speech bubble -->
      <rect x="175" y="25" width="135" height="42" rx="12" fill="#ffffff" stroke="#dd6b20" stroke-width="2"/>
      <text x="242" y="51" font-family="sans-serif" font-size="12" font-weight="bold" fill="#c05621" text-anchor="middle">豆腐多一點！</text>
      <polygon points="190,67 200,67 185,80" fill="#ffffff" stroke="#dd6b20" stroke-width="1.5"/>
      {auntie_head(160, 105, 'warm')}
    </g>
    '''
    return svg_wrap(content)

def make_auntie_eat():
    content = f'''
    <g id="auntie-eat">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#4a5568" stroke-width="16" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#4a5568" stroke-width="16" stroke-linecap="round"/>
      <path d="M115 145 L110 275 H210 L205 145 Z" fill="#dd6b20"/>
      <path d="M115 150 L110 220 L145 250" stroke="#dd6b20" stroke-width="14" stroke-linecap="round"/>
      <circle cx="145" cy="252" r="7" fill="#e6b88a"/>
      <path d="M205 150 L210 210 L175 230" stroke="#dd6b20" stroke-width="14" stroke-linecap="round"/>
      <circle cx="172" cy="230" r="7" fill="#e6b88a"/>
      <line x1="172" y1="230" x2="160" y2="155" stroke="#a0aec0" stroke-width="3" stroke-linecap="round"/>
      {mapo_bowl(160, 240)}
      {auntie_head(160, 105, 'eat')}
    </g>
    '''
    return svg_wrap(content)

def make_auntie_leave():
    content = f'''
    <g id="auntie-leave">
      <path d="M140 290 L165 385 L180 385" stroke="#4a5568" stroke-width="16" stroke-linecap="round"/>
      <path d="M180 290 L135 380 L125 380" stroke="#4a5568" stroke-width="16" stroke-linecap="round"/>
      <path d="M115 145 L105 295 H215 L205 145 Z" fill="#dd6b20"/>
      <!-- Waving goodbye with bright smile -->
      <path d="M115 150 L85 220 L75 230" stroke="#dd6b20" stroke-width="14" stroke-linecap="round"/>
      <circle cx="75" cy="235" r="7" fill="#e6b88a"/>
      <rect x="55" y="235" width="34" height="42" rx="4" fill="#ed8936"/>
      <path d="M205 150 L235 180 L240 145" stroke="#dd6b20" stroke-width="14" stroke-linecap="round"/>
      <circle cx="240" cy="140" r="7" fill="#e6b88a"/>
      {auntie_head(160, 105, 'warm')}
    </g>
    '''
    return svg_wrap(content)

# -------------------------------------------------------------
# 5. QUIET YOUTH (安靜青年)
# Minimalist knit sweater #cbd5e0, reserved posture, polite nod
# -------------------------------------------------------------
def quiet_head(cx=160, cy=105, expr='quiet'):
    mouth = f'<path d="M{cx-8} {cy+28} H{cx+8}" stroke="#742a2a" stroke-width="2.5" stroke-linecap="round"/>'
    if expr == 'eat':
        mouth = f'<ellipse cx="{cx}" cy="{cy+28}" rx="7" ry="6" fill="#742a2a"/>'
    elif expr == 'smile':
        mouth = f'<path d="M{cx-8} {cy+26} Q{cx} {cy+33} {cx+8} {cy+26}" stroke="#742a2a" stroke-width="2.5" fill="none"/>'
    
    return f'''
    <!-- Head & Neat minimalist hair -->
    <circle cx="{cx}" cy="{cy}" r="38" fill="#e6b88a"/>
    <path d="M{cx-38} {cy-2} Q{cx-35} {cy-44} {cx} {cy-42} Q{cx+35} {cy-44} {cx+38} {cy-2} Q{cx+15} {cy-18} {cx} {cy-18} Q{cx-18} {cy-18} {cx-38} {cy-2} Z" fill="#1a202c"/>
    <!-- Gentle calm eyes -->
    <path d="M{cx-18} {cy+2} Q{cx-12} {cy+6} {cx-6} {cy+2}" stroke="#1a202c" stroke-width="2.5" fill="none"/>
    <path d="M{cx+6} {cy+2} Q{cx+12} {cy+6} {cx+18} {cy+2}" stroke="#1a202c" stroke-width="2.5" fill="none"/>
    <!-- Gentle eyebrows -->
    <path d="M{cx-20} {cy-10} H{cx-8}" stroke="#2d3748" stroke-width="2"/>
    <path d="M{cx+8} {cy-10} H{cx+20}" stroke="#2d3748" stroke-width="2"/>
    {mouth}
    '''

def make_quiet_walk_in():
    content = f'''
    <g id="quiet-walk-in">
      <path d="M145 290 L135 385 L125 385" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M175 290 L185 380 L195 380" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M125 145 L118 295 H202 L195 145 Z" fill="#cbd5e0"/>
      <!-- Arms quietly at side -->
      <path d="M125 150 L110 230 L115 250" stroke="#cbd5e0" stroke-width="14" stroke-linecap="round"/>
      <circle cx="116" cy="252" r="6" fill="#e6b88a"/>
      <path d="M195 150 L210 230 L205 250" stroke="#cbd5e0" stroke-width="14" stroke-linecap="round"/>
      <circle cx="204" cy="252" r="6" fill="#e6b88a"/>
      {quiet_head(160, 105, 'quiet')}
    </g>
    '''
    return svg_wrap(content)

def make_quiet_sit():
    content = f'''
    <g id="quiet-sit">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M125 145 L120 275 H200 L195 145 Z" fill="#cbd5e0"/>
      <!-- Hands folded neatly on lap -->
      <path d="M125 150 L115 220 L150 255" stroke="#cbd5e0" stroke-width="14" stroke-linecap="round"/>
      <path d="M195 150 L205 220 L170 255" stroke="#cbd5e0" stroke-width="14" stroke-linecap="round"/>
      <circle cx="160" cy="255" r="8" fill="#e6b88a"/>
      {quiet_head(160, 105, 'quiet')}
    </g>
    '''
    return svg_wrap(content)

def make_quiet_order():
    content = f'''
    <g id="quiet-order">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M125 145 L120 275 H200 L195 145 Z" fill="#cbd5e0"/>
      <!-- Polite slight hand gesture: 中辣就好，謝謝 -->
      <path d="M125 150 L115 220 L140 250" stroke="#cbd5e0" stroke-width="14" stroke-linecap="round"/>
      <circle cx="140" cy="252" r="6" fill="#e6b88a"/>
      <path d="M195 150 L210 200 L195 180" stroke="#cbd5e0" stroke-width="14" stroke-linecap="round"/>
      <circle cx="192" cy="178" r="6" fill="#e6b88a"/>
      <!-- Small polite speech bubble -->
      <rect x="180" y="35" width="125" height="38" rx="10" fill="#ffffff" stroke="#718096" stroke-width="1.5"/>
      <text x="242" y="58" font-family="sans-serif" font-size="11" font-weight="bold" fill="#4a5568" text-anchor="middle">中辣就好……謝謝</text>
      <polygon points="195,73 205,73 190,82" fill="#ffffff" stroke="#718096" stroke-width="1.5"/>
      {quiet_head(160, 105, 'quiet')}
    </g>
    '''
    return svg_wrap(content)

def make_quiet_eat():
    content = f'''
    <g id="quiet-eat">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M125 145 L120 275 H200 L195 145 Z" fill="#cbd5e0"/>
      <path d="M125 150 L115 220 L145 250" stroke="#cbd5e0" stroke-width="14" stroke-linecap="round"/>
      <circle cx="145" cy="252" r="6" fill="#e6b88a"/>
      <path d="M195 150 L205 210 L175 230" stroke="#cbd5e0" stroke-width="14" stroke-linecap="round"/>
      <circle cx="172" cy="230" r="6" fill="#e6b88a"/>
      <line x1="172" y1="230" x2="160" y2="155" stroke="#a0aec0" stroke-width="3" stroke-linecap="round"/>
      {mapo_bowl(160, 240)}
      {quiet_head(160, 105, 'eat')}
    </g>
    '''
    return svg_wrap(content)

def make_quiet_leave():
    content = f'''
    <g id="quiet-leave">
      <path d="M145 290 L160 385 L170 385" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M175 290 L140 380 L130 380" stroke="#2d3748" stroke-width="16" stroke-linecap="round"/>
      <path d="M125 145 L118 295 H202 L195 145 Z" fill="#cbd5e0"/>
      <!-- Polite slight bow walking out -->
      <path d="M125 150 L110 230 L120 250" stroke="#cbd5e0" stroke-width="14" stroke-linecap="round"/>
      <circle cx="120" cy="252" r="6" fill="#e6b88a"/>
      <path d="M195 150 L210 230 L200 250" stroke="#cbd5e0" stroke-width="14" stroke-linecap="round"/>
      <circle cx="200" cy="252" r="6" fill="#e6b88a"/>
      {quiet_head(160, 105, 'smile')}
    </g>
    '''
    return svg_wrap(content)

# -------------------------------------------------------------
# 6. REPEAT PATRON (熟客)
# Bomber jacket #2b6cb0, relaxed posture, insider wink
# -------------------------------------------------------------
def repeat_head(cx=160, cy=105, expr='relaxed'):
    mouth = f'<path d="M{cx-10} {cy+25} Q{cx} {cy+35} {cx+12} {cy+25}" stroke="#742a2a" stroke-width="3" fill="none"/>'
    if expr == 'eat':
        mouth = f'<ellipse cx="{cx}" cy="{cy+28}" rx="8" ry="7" fill="#742a2a"/>'
    
    return f'''
    <!-- Head & Casual undercut hair -->
    <circle cx="{cx}" cy="{cy}" r="40" fill="#e6b88a"/>
    <path d="M{cx-40} {cy-5} Q{cx-36} {cy-46} {cx} {cy-45} Q{cx+38} {cy-45} {cx+40} {cy-5} Q{cx+20} {cy-18} {cx} {cy-18} Q{cx-20} {cy-18} {cx-40} {cy-5} Z" fill="#1a202c"/>
    <!-- Confident eyes (one winking!) -->
    <circle cx="{cx-15}" cy="{cy+2}" r="3.5" fill="#1a202c"/>
    <path d="M{cx+8} {cy+2} Q{cx+15} {cy-4} {cx+22} {cy+2}" stroke="#1a202c" stroke-width="3" fill="none"/>
    <!-- Eyebrows -->
    <path d="M{cx-24} {cy-14} L{cx-8} {cy-12}" stroke="#1a202c" stroke-width="3" stroke-linecap="round"/>
    <path d="M{cx+8} {cy-12} L{cx+24} {cy-14}" stroke="#1a202c" stroke-width="3" stroke-linecap="round"/>
    {mouth}
    '''

def make_repeat_walk_in():
    content = f'''
    <g id="repeat-walk-in">
      <path d="M145 290 L125 385 L115 385" stroke="#1a202c" stroke-width="18" stroke-linecap="round"/>
      <path d="M175 290 L195 380 L210 380" stroke="#1a202c" stroke-width="18" stroke-linecap="round"/>
      <!-- Blue bomber jacket over white tee -->
      <path d="M120 145 L110 295 H210 L200 145 Z" fill="#2b6cb0"/>
      <polygon points="148,145 172,145 160,205" fill="#edf2f7"/>
      <!-- Hands in jacket pockets casual stride -->
      <path d="M120 150 L95 230 L118 260" stroke="#2b6cb0" stroke-width="16" stroke-linecap="round"/>
      <path d="M200 150 L225 230 L202 260" stroke="#2b6cb0" stroke-width="16" stroke-linecap="round"/>
      {repeat_head(160, 105, 'relaxed')}
    </g>
    '''
    return svg_wrap(content)

def make_repeat_sit():
    content = f'''
    <g id="repeat-sit">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#1a202c" stroke-width="18" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#1a202c" stroke-width="18" stroke-linecap="round"/>
      <path d="M120 145 L115 275 H205 L200 145 Z" fill="#2b6cb0"/>
      <polygon points="148,145 172,145 160,205" fill="#edf2f7"/>
      <!-- Relaxed arm draped on chair armrest -->
      <path d="M120 150 L90 220 L120 255" stroke="#2b6cb0" stroke-width="16" stroke-linecap="round"/>
      <circle cx="122" cy="258" r="8" fill="#e6b88a"/>
      <path d="M200 150 L230 220 L200 255" stroke="#2b6cb0" stroke-width="16" stroke-linecap="round"/>
      <circle cx="198" cy="258" r="8" fill="#e6b88a"/>
      {repeat_head(160, 105, 'relaxed')}
    </g>
    '''
    return svg_wrap(content)

def make_repeat_order():
    content = f'''
    <g id="repeat-order">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#1a202c" stroke-width="18" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#1a202c" stroke-width="18" stroke-linecap="round"/>
      <path d="M120 145 L115 275 H205 L200 145 Z" fill="#2b6cb0"/>
      <!-- Finger pointing: 一樣的，今天再辣一點！ -->
      <path d="M120 150 L95 210 L125 240" stroke="#2b6cb0" stroke-width="16" stroke-linecap="round"/>
      <circle cx="126" cy="242" r="8" fill="#e6b88a"/>
      <path d="M200 150 L230 180 L220 150" stroke="#2b6cb0" stroke-width="16" stroke-linecap="round"/>
      <circle cx="220" cy="148" r="8" fill="#e6b88a"/>
      <rect x="175" y="25" width="135" height="42" rx="12" fill="#ffffff" stroke="#2b6cb0" stroke-width="2"/>
      <text x="242" y="51" font-family="sans-serif" font-size="12" font-weight="bold" fill="#2b6cb0" text-anchor="middle">熟客配方 · 再辣一點</text>
      <polygon points="190,67 200,67 185,80" fill="#ffffff" stroke="#2b6cb0" stroke-width="1.5"/>
      {repeat_head(160, 105, 'relaxed')}
    </g>
    '''
    return svg_wrap(content)

def make_repeat_eat():
    content = f'''
    <g id="repeat-eat">
      {clinic_chair(160, 270)}
      <path d="M135 270 L130 350 L120 375" stroke="#1a202c" stroke-width="18" stroke-linecap="round"/>
      <path d="M185 270 L190 350 L200 375" stroke="#1a202c" stroke-width="18" stroke-linecap="round"/>
      <path d="M120 145 L115 275 H205 L200 145 Z" fill="#2b6cb0"/>
      <path d="M120 150 L110 220 L145 250" stroke="#2b6cb0" stroke-width="16" stroke-linecap="round"/>
      <circle cx="145" cy="252" r="8" fill="#e6b88a"/>
      <path d="M200 150 L210 210 L175 230" stroke="#2b6cb0" stroke-width="16" stroke-linecap="round"/>
      <circle cx="172" cy="230" r="8" fill="#e6b88a"/>
      <line x1="172" y1="230" x2="160" y2="155" stroke="#a0aec0" stroke-width="3" stroke-linecap="round"/>
      {mapo_bowl(160, 240)}
      {repeat_head(160, 105, 'eat')}
    </g>
    '''
    return svg_wrap(content)

def make_repeat_leave():
    content = f'''
    <g id="repeat-leave">
      <path d="M145 290 L165 385 L180 385" stroke="#1a202c" stroke-width="18" stroke-linecap="round"/>
      <path d="M175 290 L135 380 L125 380" stroke="#1a202c" stroke-width="18" stroke-linecap="round"/>
      <path d="M120 145 L110 295 H210 L200 145 Z" fill="#2b6cb0"/>
      <!-- Satisfied regular giving salute wave -->
      <path d="M120 150 L95 230 L115 260" stroke="#2b6cb0" stroke-width="16" stroke-linecap="round"/>
      <path d="M200 150 L235 180 L230 140" stroke="#2b6cb0" stroke-width="16" stroke-linecap="round"/>
      <circle cx="230" cy="136" r="8" fill="#e6b88a"/>
      {repeat_head(160, 105, 'relaxed')}
    </g>
    '''
    return svg_wrap(content)

# ----------------- Write Files -----------------

patients_data = {
    'patient_office': {
        'walk_in': make_office_walk_in(),
        'sit': make_office_sit(),
        'order': make_office_order(),
        'eat': make_office_eat(),
        'leave': make_office_leave(),
    },
    'patient_student': {
        'walk_in': make_student_walk_in(),
        'sit': make_student_sit(),
        'order': make_student_order(),
        'eat': make_student_eat(),
        'leave': make_student_leave(),
    },
    'patient_driver': {
        'walk_in': make_driver_walk_in(),
        'sit': make_driver_sit(),
        'order': make_driver_order(),
        'eat': make_driver_eat(),
        'leave': make_driver_leave(),
    },
    'patient_auntie': {
        'walk_in': make_auntie_walk_in(),
        'sit': make_auntie_sit(),
        'order': make_auntie_order(),
        'eat': make_auntie_eat(),
        'leave': make_auntie_leave(),
    },
    'patient_quiet': {
        'walk_in': make_quiet_walk_in(),
        'sit': make_quiet_sit(),
        'order': make_quiet_order(),
        'eat': make_quiet_eat(),
        'leave': make_quiet_leave(),
    },
    'patient_repeat': {
        'walk_in': make_repeat_walk_in(),
        'sit': make_repeat_sit(),
        'order': make_repeat_order(),
        'eat': make_repeat_eat(),
        'leave': make_repeat_leave(),
    }
}

count = 0
for pat_id, states in patients_data.items():
    for state_name, svg_content in states.items():
        fname = f"{pat_id}_{state_name}.svg"
        fpath = OUT_DIR / fname
        fpath.write_text(svg_content.strip(), encoding='utf-8')
        count += 1
        print(f"Wrote {fname}")

print(f"Total patient assets generated: {count}")
