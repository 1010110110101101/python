import pygame
from pygame.locals import *
from time import sleep
import time
import random

pygame.font.init()
myfont = pygame.font.SysFont("monospace", 15)
myfontgold = pygame.font.SysFont("monospace", 18)

black = (0, 0, 0)
done = False

multi = 1
gold = 100
ario = 0
cario = 0
paper = 0
bank = 0

ario_cost = 100
cario_cost = 350
paper_cost = 500
bank_cost = 1000

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
keys = {"a":False, "c":False, "p":False, "b":False}
pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

while not done:
    screen.fill(black)
    clock.tick(60)
    # Event handler
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == KEYDOWN:
            #Buy Ario
            if event.key == K_a:
                if gold >= ario_cost:
                    gold = gold - ario_cost
                    multi += 1
                    ario += 1
                    ario_cost += 25
                keys["a"] = True
                
            #Buy Company(Ario)
            if event.key == K_c:
                if gold >= cario_cost:
                    gold = gold - cario_cost
                    multi += 2
                    cario += 1
                    cario_cost += 50
                keys["c"] = True
            #Buy Paper Mill
            if event.key == K_p:
                if gold >= paper_cost:
                    gold = gold - paper_cost
                    multi += 2
                    paper += 1
                    paper_cost += 25
                keys["p"] = True
            #Buy Bank
            if event.key == K_b:
                if gold >= bank_cost:
                    gold = gold - bank_cost
                    multi += 5
                    bank += 1
                    bank_cost += 175
                keys["b"] = True
                
        elif event.type == pygame.USEREVENT + 1:
            gold += (1.5 * multi) - 0.5

    #Text    
    label = myfontgold.render("Gold: " + str(gold), 50, (255, 215, 0))
    invest = myfont.render("Investments: ", 30, (25, 255, 25))
    hint = myfont.render("To buy investments, press the first leter of the investement.", 20, (200, 200, 200))
    
    #Purchase list
    Ario = myfont.render("Ario Investments: " + str(ario), 10, (25, 255, 25))
    Ario_cost = myfont.render("(Cost: " + str(ario_cost) + ")", 10, (25, 255, 25))
    Company = myfont.render("Company(Ario) Investments: " + str(cario), 10, (35, 255, 35))
    Company_cost = myfont.render("(Cost: " + str(cario_cost) + ")", 10, (35, 255, 35))
    Paper = myfont.render("Paper Mill Investments: " + str(paper), 10, (45, 255, 45))
    Paper_cost = myfont.render("(Cost: " + str(paper_cost) + ")", 10, (45, 255, 45))
    Bank = myfont.render("Bank Investments: " + str(bank), 10, (55, 255, 55))
    Bank_cost = myfont.render("(Cost: " + str(bank_cost) + ")", 10, (55, 255, 55))
    
    #Text render
    screen.blit(label, (10, 10))
    screen.blit(invest, (200, 20))
    screen.blit(hint, (10, 460))
    
    #Purchase list render
    screen.blit(Ario, (220, 35))
    screen.blit(Ario_cost, (600, 35))
    screen.blit(Company, (220, 50))
    screen.blit(Company_cost, (600, 50))
    screen.blit(Paper, (220, 65))
    screen.blit(Paper_cost, (600, 65))
    screen.blit(Bank, (220, 80))
    screen.blit(Bank_cost, (600, 80))
    
    pygame.display.flip()
pygame.quit()

