# LiteRT Inference with Webcam

## Usage

Tested on Raspberry Pi 5 with USB Webcam.

After cloning,

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements-lite.txt`
4. Copy in your `.tflite` model from [Prelab](https://usafa-ece.github.io/ece386-book/b3-devboard/lab-cat-dog.html#pre-lab)
5. `python litert_continuous.py cat-dog-mnv2.tflite`

Verify your signatures are what you expect, then get to work!

## Discussion Questions
### 1. Relative Model Sizes
### 2. Relative Performance for more vs. Fewer images per run, and why
### 3. Pipeline stalls waiting for memory
### 4. L2 Invalidations (overwrites of memory)
### 5. LLC Loads and Misses

## Documentation
We used chatGPT to help us figure out how to connect a webcam. It told us to cycle through the initialization (0-9) which we did and eventually found that our webcam was floating around in the 7-10 range depending on the time. 

### People
C1Cs Matthew Westbrook and Alex White

### LLMs
ChatGPT usage for 
