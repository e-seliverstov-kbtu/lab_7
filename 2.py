import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
done = False
is_blue = True

SONG_END = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(SONG_END)

music_list = ['song_1.mp3', 'song_2.mp3', 'song_3.mp3']

currently_playing_song = 0
music_started = False
clock = pygame.time.Clock()
color = (255, 0 , 0)
pygame.mixer.music.load(music_list[currently_playing_song])
paused = 0
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == SONG_END:
                        currently_playing_song = (currently_playing_song + 1) % len(music_list)
                        pygame.mixer.music.load(music_list[currently_playing_song])
                        pygame.mixer.music.play(0)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    pygame.mixer.music.play(0)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    if paused == 0:
                        pygame.mixer.music.pause()
                        paused = 1
                    else:
                        if music_started == False:
                            pygame.mixer.music.play()
                            music_started = True
                        else:
                            pygame.mixer.music.unpause()
                        paused = 0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    currently_playing_song = (currently_playing_song - 1) % len(music_list)
                    pygame.mixer.music.load(music_list[currently_playing_song])
                    if paused == 0:
                        pygame.mixer.music.play(0)
                    else:
                        music_started = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    currently_playing_song = (currently_playing_song + 1) % len(music_list)
                    pygame.mixer.music.load(music_list[currently_playing_song])
                    if paused == 0:
                        pygame.mixer.music.play(0)
                    else:
                        music_started = False

            
        screen.fill((0, 0, 0))
        pygame.display.flip()



pygame.quit()
sys.exit()

