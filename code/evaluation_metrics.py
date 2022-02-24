#!/usr/bin/env python
# coding: utf-8

import numpy as np
import math


def r_precision(test, recs):
    """
    R-precision is the number of retrieved relevant tracks divided by the number of known relevant tracks 
    (i.e., the number of withheld tracks)
    The metric is averaged across all playlists in the challenge set. 
    This metric rewards total number of retrieved relevant tracks (regardless of order).
    """
    r_pres = [single_r_precition(pl, rec) for pl, rec in zip(test, recs)]
    return np.mean(r_pres)


def single_r_precition(pl, rec):
    return sum([1 for s in rec if s[0] in pl]) / len(pl)


def NDCG(test, recs):
    """
    Discounted Cumulative Gain (DCG) measures the ranking quality of the recommended tracks, 
    increasing when relevant tracks are placed higher in the list. 
    Normalized DCG (NDCG) is determined by calculating the DCG and dividing it 
    by the ideal DCG in which the recommended tracks are perfectly ranked.
    
    This implementation is of a simple Implicit NDCG.
    """
    ndcgs = [single_NDCG(pl, rec) for pl, rec in zip(test, recs)]
    return np.mean(ndcgs)
  
    
def single_NDCG(pl, rec):
    for i, s in enumerate(rec):
        if s[0] in pl:
            return math.log(2) / math.log(i + 2)
        
    return 0


def recommended_songs_clicks(test, recs):
    """
    Recommended Songs is a Spotify feature that, given a set of tracks in a playlist, 
    recommends 10 tracks to add to the playlist. 
    The list can be refreshed to produce 10 more tracks. 
    Recommended Songs clicks is the number of refreshes needed before a relevant track is encountered.
    If the metric does not exist (i.e. if there are no relevant tracks in R
    a value of 11 is picked (which is 1 greater than the maximum number of clicks possible).
    """
    rscs = [single_recommended_songs_clicks(pl, rec) for pl, rec in zip(test, recs)]
    return np.mean(rscs)


def single_recommended_songs_clicks(pl, rec):
    for i, s in enumerate(rec):
        if s[0] in pl:
            return int((i + 1) / 10)
    
    return 11

