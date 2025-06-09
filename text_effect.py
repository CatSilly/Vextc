import time 
import sys
import itertools
from typing import Optional

# Type 1
def delay_print(text, delay):
    time.sleep(delay)
    print(text)
    
# Type 2
def slow_print(text, speed):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()
    
# Type 3
def loading_anima(dur=5):
  
    animation_symbols = itertools.cycle(['|', '/', '-', '\\'])
    end_time = time.time() + dur
    
    while time.time() < end_time:
        current_symbol = next(animation_symbols)
        print(f'\rLoading {current_symbol}', end='', flush=True)
        time.sleep(0.1)
    
    print('\rLoading complete!')

# Type 4
def scrolling_text(
    text: str, 
    display_width: int = 20, 
    scroll_delay: float = 0.2
) -> None:
    
    padding = ' ' * display_width
    scrolling_content = f"{padding}{text}{padding}"
    
    for position in range(len(scrolling_content) - display_width):
        print(scrolling_content[position:position + display_width], end='\r')
        time.sleep(scroll_delay)
    
    print()