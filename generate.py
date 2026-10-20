import json
from pathlib import Path

with open('chara_model.json') as f:
    model = json.load(f)

svg = '''<svg width='400' height='600' xmlns='http://www.w3.org/2000/svg'>
    <!-- Background -->
    <rect width='400' height='600' fill='#2a2a2a'/>
    
    <!-- Shadow -->
    <ellipse cx='200' cy='520' rx='70' ry='20' fill='#000' opacity='0.3'/>
    
    <!-- Legs (pants) -->
    <g id='legs'>
        <rect x='170' y='420' width='25' height='100' rx='5' fill='#8b4513' stroke='#654321' stroke-width='2'/>
        <rect x='205' y='420' width='25' height='100' rx='5' fill='#8b4513' stroke='#654321' stroke-width='2'/>
        <ellipse cx='182.5' cy='525' rx='18' ry='10' fill='#2f1b0f' stroke='#1a0e08' stroke-width='1.5'/>
        <ellipse cx='217.5' cy='525' rx='18' ry='10' fill='#2f1b0f' stroke='#1a0e08' stroke-width='1.5'/>
    </g>
    
    <!-- Body (torso) -->
    <g id='torso'>
        <path d='M 170 250 L 150 400 L 170 420 L 205 420 L 230 420 L 250 400 L 230 250 Z' 
              fill='#dc143c' stroke='#8b0000' stroke-width='2'/>
        <line x1='175' y1='280' x2='225' y2='280' stroke='#228b22' stroke-width='12'/>
        <line x1='165' y1='300' x2='235' y2='300' stroke='#228b22' stroke-width='12'/>
        <line x1='158' y1='320' x2='242' y2='320' stroke='#228b22' stroke-width='12'/>
        <line x1='153' y1='340' x2='247' y2='340' stroke='#228b22' stroke-width='12'/>
        <line x1='150' y1='360' x2='250' y2='360' stroke='#228b22' stroke-width='12'/>
        <line x1='155' y1='380' x2='245' y2='380' stroke='#228b22' stroke-width='12'/>
        <line x1='162' y1='400' x2='238' y2='400' stroke='#228b22' stroke-width='12'/>
        <ellipse cx='155' cy='320' rx='20' ry='65' fill='#dc143c' stroke='#8b0000' stroke-width='2' transform='rotate(-20 155 320)'/>
        <ellipse cx='245' cy='320' rx='20' ry='65' fill='#dc143c' stroke='#8b0000' stroke-width='2' transform='rotate(20 245 320)'/>
        <circle cx='140' cy='370' r='16' fill='#fdbcb4' stroke='#e6a295' stroke-width='1.5'/>
        <circle cx='260' cy='370' r='16' fill='#fdbcb4' stroke='#e6a295' stroke-width='1.5'/>
    </g>
    
    <!-- Neck -->
    <rect x='185' y='230' width='30' height='25' rx='8' fill='#fdbcb4' stroke='#e6a295' stroke-width='1.5'/>
    
    <!-- Head -->
    <circle cx='200' cy='160' r='80' fill='#fdbcb4' stroke='#e6a295' stroke-width='2'/>
    
    <!-- Hair -->
    <g id='hair'>
        <path d='M 125 160 Q 120 250 135 280 Q 145 320 160 340 Q 175 360 200 365 Q 225 360 240 340 Q 255 320 265 280 Q 280 250 275 160 Q 275 130 250 110 Q 220 95 200 95 Q 180 95 150 110 Q 125 130 125 160 Z'
              fill='#6b4423' stroke='#4a2c18' stroke-width='2'/>
        <path d='M 125 150 Q 115 200 120 240 Q 125 220 130 200 L 135 160 Z' fill='#6b4423' stroke='#4a2c18' stroke-width='1.5'/>
        <path d='M 275 150 Q 285 200 280 240 Q 275 220 270 200 L 265 160 Z' fill='#6b4423' stroke='#4a2c18' stroke-width='1.5'/>
        <path d='M 140 120 Q 170 105 200 105 Q 230 105 260 120 Q 245 140 200 145 Q 155 140 140 120 Z'
              fill='#6b4423' stroke='#4a2c18' stroke-width='2'/>
    </g>
    
    <!-- Eyes -->
    <g id='eyes'>
        <circle cx='170' cy='150' r='12' fill='white'/>
        <circle cx='230' cy='150' r='12' fill='white'/>
        <circle cx='170' cy='150' r='6' fill='#dc143c'/>
        <circle cx='230' cy='150' r='6' fill='#dc143c'/>
        <path d='M 158 138 Q 170 132 182 138' stroke='#4a2c18' stroke-width='3' fill='none'/>
        <path d='M 218 138 Q 230 132 242 138' stroke='#4a2c18' stroke-width='3' fill='none'/>
    </g>
    
    <!-- Mouth -->
    <path d='M 190 175 Q 200 185 210 175' stroke='#a0522d' stroke-width='2.5' fill='none'/>
    
    <!-- Blush -->
    <ellipse cx='150' cy='170' rx='10' ry='5' fill='#ffb6c1' opacity='0.5'/>
    <ellipse cx='250' cy='170' rx='10' ry='5' fill='#ffb6c1' opacity='0.5'/>
</svg>'''

Path('chara.svg').write_text(svg)
