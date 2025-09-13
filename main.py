import win32api, win32con, win32gui, ctypes
# def get_window_pos(name):
#     name = name
#     handle = win32gui.FindWindow(0, name)
#     if handle == 0:
#         return None
#     else:
#         return win32gui.GetWindowRect(handle)
def get_window_pos(hwnd):
    try:
        f = ctypes.windll.dwmapi.DwmGetWindowAttribute
    except:
        f = None
    if f:
        rect = ctypes.wintypes.RECT()
        DWMWA_EXTENDED_FRAME_BOUNDS = 9
        f(ctypes.wintypes.HWND(hwnd),
          ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
          ctypes.byref(rect),
          ctypes.sizeof(rect))
        return rect.left, rect.top, rect.right, rect.bottom
from PIL import Image, ImageGrab

# while True:
# t = get_window_pos("文件资源管理器")
# print(t)
# img_ready = ImageGrab.grab(t)
# img_ready.show()
# while True:
#     pass

import pygame, sys
pygame.init()
win = pygame.display.set_mode((1200, 800))

py_img = None
def proc():
    img = get_window_pos(win32gui.FindWindow(0, "文件资源管理器"))
    img = ImageGrab.grab(img)
    if img == None:
        return
    mode = img.mode
    size = img.size
    data = img.tobytes()
    global py_img
    try:
        py_img = pygame.image.fromstring(data, size, mode)
    except:
        py_img = None

FPS = 10
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
    clock.tick(FPS)
    proc()
    
    win.fill((255, 255, 255))
    if py_img != None:
        win.blit(py_img, (10, 10))
    pygame.display.flip()