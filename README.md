# song-rec-project
Song recommendation using song embeddings and encoder-decoder NN

The data used is from Here:
https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge

The project is inspired by:
https://arxiv.org/abs/1606.07154

Implementing Song2Vec using Word2Vec algorithm.
Using the embeddings, the project tries 3 recommending methods:
- Searching for most similar songs using Cosine Similarity on song embeddings.
- Using K-Means recommending only songs from most likely clusters.
- Using a novel Neural Network approach of Encoder-Decoder to predict the embedding of the next song and searching for most similar song embeddings to the predicted vector.

## Dataset:
In order to run the project one needs to firstly download the Dataset from the link above.

## Requirements:
The project was written in python 3.7.
It uses the following libraries:
- numpy
- pandas
- matplotlib
- tensorflow
- keras
- gensim

## Running the project:
The research is written in notebooks.
The order of the notebooks is as follows:
- spotify_data_preperation: where the raw data is parsed and saved as train and test files.
- song2vec: where the song embeddings are created and hyper-parameters are tested.
- embeddings_to_embeddings_model-hyper-parameters (optional): where the novel DNN encoder-decoder model is created and hyper-parameters are tested.
- embeddings_to_embeddings_model-final: where the final Encoder-Decoder model is created and saved.
- recommendation: where the final recommending functions using the models are created and all methods are evaluated.
- data_exploration (optional): where the Spotify dataset is explored. 

In addition, there is another python module:
- evaluation_metrics: where two evaluation methods are created. The evaluation methods are the one recommended by Spotify for the Dataset.
