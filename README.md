This repository contains my submission for the CS779 Competition: Machine Translation System for India, conducted at IIT Kanpur.
The goal was to build train-from-scratch Neural Machine Translation (NMT) systems for English → Hindi (EN→HI) and English → Bengali (EN→BN) under strict constraints.

Author

Name: Sunny Raja Prasad

Roll No: 218171078

Institute: Indian Institute of Technology Kanpur

Email: sunnyrp21@iitk.ac.in

Project Overview

The task involved building an encoder–decoder NMT system using only the provided data, no pretrained language models, and PyTorch-only implementations.

After experimenting with:

Seq2Seq (no attention)

Seq2Seq + Attention

Transformer (trained from scratch)

the final submitted model was an 8-layer Convolutional Sequence-to-Sequence (ConvS2S) architecture with attention.

Competition Results
Phase	Rank	chrF++	ROUGE	BLEU
Development	31	0.385	0.404	0.138
Test	46	0.390	0.418	0.143

Codabench Username: s_218171078

Training Submissions: 18

Test Submissions: 7

Key Features

Architecture: Convolutional Seq2Seq (ConvS2S)

Encoder / Decoder: 8 convolutional layers each

Embedding Dimension: 512

Hidden Dimension: 512

Kernel Size: 3

Attention: Scaled dot-product attention at every decoder layer

Decoding: Batched greedy decoding

Framework: PyTorch (from scratch)

Data & Preprocessing

Languages: EN→HI, EN→BN

Tokenization: Word-level (nltk.word_tokenize)

Vocabulary: Minimum frequency = 2

Special Tokens: <PAD>, <SOS>, <EOS>, <UNK>

Max Sequence Length: 64

Text Cleaning:

Lowercasing

Unicode normalization (NFC)

Removal of punctuation and digits

Whitespace normalization

⚠️ Note: Word-level tokenization caused a large OOV (Out-of-Vocabulary) problem, especially for named entities.

Training Details

Loss: Cross-Entropy (padding ignored)

Optimizer: Adam

Learning Rate: 5e-4

LR Scheduler: ReduceLROnPlateau

Batch Size: 32

Dropout: 0.25

Gradient Clipping: ‖g‖₂ ≤ 1

Teacher Forcing: 1.0 (constant)

Checkpointing: Best validation-loss model only

Inference

Decoding Strategy: Greedy search

Stopping Criterion: <EOS> token or max length

Detokenization: Simple whitespace join

Greedy decoding was chosen for speed, though it introduces repetition and early-stopping errors.

Error Analysis Summary

Main error sources:

OOV & Named Entities — due to word-level vocabulary

Missing digits & punctuation — removed during preprocessing

Repetitions & brevity — caused by greedy decoding

Long-distance dependencies — limited by convolution kernel size

Lessons Learned

Preprocessing choices are critical — removing punctuation/digits significantly harms translation quality.

Word-level tokenization is a bottleneck — it leads to massive OOV issues.

Greedy decoding trades quality for speed — beam search would substantially improve results.

Future Improvements

Replace word-level tokenization with SentencePiece (BPE/Unigram)

Implement Beam Search with length normalization

Preserve punctuation and digits

Explore copy/transliteration mechanisms for named entities

Compare optimized ConvS2S vs BiLSTM + Attention with subwords

References

Sutskever et al., Sequence to Sequence Learning with Neural Networks

Bahdanau et al., Neural Machine Translation by Jointly Learning to Align and Translate

Vaswani et al., Attention Is All You Need

Kunchukuttan & Bhattacharyya, MT for Indian Languages
