#!/bin/bash
# autor: Felipe Moraes email: lipe12302@gmail.com
# descricao: aplicacao simples de CLI para downloads de videos do YouTube.
from pytube import YouTube

while True:
    print("BAIXADOR DE VIDEOS DO YOUTUBE\n")
    link = input("COLE AQUI O LINK DO VIDEO: \n>:")
    caminho = input("INFORME A PASTA PARA DOWNLOAD: \n>:")
    YouTube(link).streams.first().download(caminho)
    print("DOWNLOAD CONCLUIDO NO CAMINHO ", caminho)
    break
