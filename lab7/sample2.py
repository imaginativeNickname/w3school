import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((300, 100))
pygame.display.set_caption("Music player")

music_files = ["bla-bla-bla-ble-ble-ble-blu-blu-blu-made-with-Voicemod.mp3", "Betsy feat. Мария Янковская - Сигма Бой.mp3","indian-music-made-with-Voicemod.mp3","gangnam-style-made-with-Voicemod.mp3","brainrot-music-made-with-Voicemod.mp3"]
current_track = 0
pygame.mixer.music.load(music_files[current_track])

running = True


def play_next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

def play_previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                play_next_track()
            elif event.key == pygame.K_LEFT:
                play_previous_track()
            elif event.key == pygame.K_UP:
                current_volume = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(min(1.0, current_volume + 0.1))
            elif event.key == pygame.K_DOWN:
                current_volume = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(max(0.0, current_volume - 0.1))

    pygame.display.flip()

pygame.quit()