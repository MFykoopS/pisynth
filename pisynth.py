#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyo import *
import pygame
from pygame.locals import *
from time import sleep

running = True
s = Server(duplex = 0)
s.boot()
pygame.init()
window = pygame.display.set_mode((100, 100))
s.start()

att = .01
dec = .2
sus = .5
rel = .1
f = Adsr(attack=att, decay=dec, sustain=sus, release=rel)
a = Sine(mul=f)
b = a.mix(2).out()

while running:
	for event in pygame.event.get():
		if (event.type == KEYDOWN):
			if event.key == K_a:
				a.setFreq([261.63,261.63])
				f.play()
			elif event.key == K_s:
				a.setFreq([293.66,293.66])
				f.play()
			elif event.key == K_d:
				a.setFreq([329.63,329.63])
				f.play()
			elif event.key == K_f:
				a.setFreq([349.23,349.23])
				f.play()
			elif event.key == K_g:
				a.setFreq([392.00,392.00])
				f.play()
			elif event.key == K_h:
				a.setFreq([440.00,440.00])
				f.play()
			elif event.key == K_j:
				a.setFreq([493.88,493.88])
				f.play()
			elif event.key == K_k:
				a.setFreq([523.25,523.25])
				f.play()
                        if pygame.key.get_mods() & KMOD_SHIFT:
                                mult = 10
                        else:
                                mult = 1
			if event.key == K_UP:
				att += .01*mult
				f.setAttack(att)
				print "Attack:", att
			elif (event.key == K_DOWN and att > 0):
				if att <= .01*mult:
					att = 0
				else:
					att -= .01*mult
				f.setAttack(att)
				print "Attack:", att
			elif (event.key == K_0 and att > 0):
				att = 0
				print "Attack:", att
			if event.key == K_ESCAPE:
				running = False
		elif (event.type == KEYUP): # this is problematic!!
		 	f.stop()
	sleep(0.0001)
pygame.quit()
