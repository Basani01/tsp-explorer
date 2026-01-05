import pygame
import sys
import random
import math
from city import City
from AIAgent import Searchagent
from gui import GUI

pygame.init()
#setup interface
width = 800
height = 600


screenwindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("TSP Explorer")

# Colors
Black = (0, 0, 0)
Orange = (255, 69, 0)
WHITE = (255, 255, 255)
blue = (50, 150, 255)
green = (2, 255, 0)

font = pygame.font.SysFont(None, 24)

# Varibles for displaying distance
PDistanceShow = None
Agentdistance = None
showwinner = None

# City generation
num_of_cities = 10
names_of_cities = ["JHB", "PLK", "CPT", "Durban", "Tzaneen", "Pretoria", "Mahikeng", "Nelspruit", "Kimberly", "Bloem"]
cities = [City(random.randint(50, width - 50), 
         random.randint(50, height - 50), 
          i, names_of_cities[i]) for i in range(num_of_cities)]


PPath = []  #player's path
AIPath = []  # agen't path
agentalreadyran = False

def draw_text(text, pos, color=WHITE):
    rendered_text = font.render(text, True, color)
    screenwindow.blit(rendered_text, pos)

def drawcities():
    screenwindow.fill(Black)

    #this is the player parth with the aguments screen, color, startpoint, next point, size of the line
    for i in range(len(PPath) - 1):
        pygame.draw.line(screenwindow, blue, PPath[i].get_pos(), PPath[i + 1].get_pos(), 3)

    # This is the ai path
    for i in range(len(AIPath) - 1):
        pygame.draw.line(screenwindow, green, AIPath[i].get_pos(), AIPath[i + 1].get_pos(), 2)

    # Draw cities
    for city in cities:
        city.draw(screenwindow)

    # Show distances and winner
    if PDistanceShow:
        draw_text(PDistanceShow, (20, 20), blue)
    if Agentdistance:
        draw_text(Agentdistance, (20, 50), green)
    if showwinner:
        draw_text(showwinner, (20, 80), WHITE)

    pygame.display.flip()

def getcity(pos):
    for city in cities:
        if city.isclicked(pos):
            return city
    return None

def main():
    #global variables for displaying the results 
    global AIPath, agentalreadyran, PDistanceShow, Agentdistance, showwinner
    clock = pygame.time.Clock()
    running = True

    def total_distance(path):
        dist = 0
        for i in range(len(path) - 1):
            dx = path[i].x - path[i + 1].x
            dy = path[i].y - path[i + 1].y
            dist += math.sqrt(dx * dx + dy * dy)
        return dist

    while running:
        clock.tick(60)
        drawcities()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_city = getcity(pos)
                if clicked_city and clicked_city not in PPath:
                    PPath.append(clicked_city)

                    if len(PPath) == len(cities) and not agentalreadyran:
                        # Close loop
                        if PPath[0] != PPath[-1]:
                            PPath.append(PPath[0])

                        # Run AI
                        agent = Searchagent(cities)
                        AIPath = agent.findway()
                        agentalreadyran = True

                        # Compute distances
                        player_distance = total_distance(PPath)
                        ai_distance = total_distance(AIPath)

                        PDistanceShow = f"Player Distance: {player_distance:.2f}"
                        Agentdistance = f"AI Distance: {ai_distance:.2f}"

                        print("\nPlayer Path:")
                        print(" -> ".join(str(city.name) for city in PPath))
                        print(PDistanceShow)

                        print("\nAI Path:")
                        print(" -> ".join(str(city.name) for city in AIPath))
                        print(Agentdistance)

                        # Determine winner
                        if player_distance < ai_distance:
                            showwinner = "🥳HOORAY! You are the winner! (Player)"
                        elif player_distance > ai_distance:
                            showwinner = "🦾 AI Agent Wins!"
                        else:
                            showwinner = "Well Done! It's a tie!"

                        print("\n" + showwinner)
                        
                        #player  agent route names, from which city to which city
                        PPath_Names = [city.name for city in PPath]  
                        AgentPath_Names = [city.name for city in AIPath]

                     
                        GUI.showresults(player_distance, ai_distance, showwinner,  PPath_Names,  AgentPath_Names)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
