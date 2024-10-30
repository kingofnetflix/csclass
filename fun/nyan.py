#!/usr/bin/env python
# encoding: utf-8
try:
    from frame import frames
except ImportError as e:
    print(f"Error importing frames: {e}")
    frames = None  # or handle the error as needed

import subprocess
import time

class Nyancat(object):
    FRAME_HEIGHT = FRAME_WIDTH = 64  # frame size
    COLORS = {
            ',' :  "\033[48;5;17m",
            '.' :  "\033[48;5;231m",
            '\'':  "\033[48;5;16m",
            '@' :  "\033[48;5;230m",
            '$' :  "\033[48;5;175m",
            '-' :  "\033[48;5;162m",
            '>' :  "\033[48;5;196m",
            '&' :  "\033[48;5;214m",
            '+' :  "\033[48;5;226m",
            '#' :  "\033[48;5;118m",
            '=' :  "\033[48;5;33m",
            ';' :  "\033[48;5;19m",
            '*' :  "\033[48;5;240m",
            '%' :  "\033[48;5;175m"
    }
    def __init__(self):
        self.terminal_height, self.terminal_width = self.linesnum()
        self.min_col = (self.FRAME_WIDTH - self.terminal_width/2) / 2
        self.max_col = (self.FRAME_WIDTH + self.terminal_width/2) / 2
        self.min_row = (self.FRAME_HEIGHT - (self.terminal_height-1)) / 2
        self.max_row = (self.FRAME_HEIGHT + (self.terminal_height-1)) / 2
        self.output = ' '
        self.clear_screen = 1  #TODO
        self.always_escape = 0  #TODO

    def linesnum(self):
        '''测试屏幕显示行数,每行字符数'''
        num = subprocess.check_output('stty size', shell=True).split()
        return int(num[0]), int(num[1])

    def run(self):
        if frames is None:
            print("Frames not available. Exiting.")
            return

        rainbow = ",,>>&&&+++###==;;;,,"
        i = 0  # frame
        last = 0

        while True:
            print('\033[?25l]')
            for y in range(self.min_row, self.max_row):
                for x in range(self.min_col, self.max_col):
                    if  23 < y < 43 and x < 0:
                        mod_x = ((-x+2) % 16) / 8;
                        if (i / 2) % 2: mod_x = 1 - mod_x;
                        tmp = mod_x + y - 23
                        if -1 < tmp < len(rainbow):
                            color = rainbow[tmp]
                        else:
                            color = ','
                    elif x < 0 or y < 0 or y >= self.FRAME_HEIGHT or x >= self.FRAME_WIDTH:
                        color = ','
                    else:
                        color = frames[i][y][x]
                    if self.always_escape:
                        print(self.COLORS[color], end=' ')
                    else:
                        if color != last and color in self.COLORS:
                            last = color;
                            print(self.COLORS[color] + self.output, end=' ')
                        else:
                            print(self.output, end=' ')
                print()
            i += 1
            if i == 11: i = 0
            last = 0
            time.sleep(0.1)
    def __del__(self):
        print('\033[?25h]')

def main():
    nyancat = Nyancat()
    nyancat.run()

if __name__ == '__main__':
    main()
