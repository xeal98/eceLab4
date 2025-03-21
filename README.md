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
### 1. Overall Discussion
### 2. Relative Model Sizes
The keras model is roughly 10x larger than the LiteRT model. With the keras model being 27 MB and the LiteRT model being 2.4 MB. This means that the LiteRT model nearly fully fits in the 2MB of L2 CPU Cache and leads to far fewer misses (discussed later in Q5). The LiteRT model uses optimizations like quantization or pruning of parameters to get to that smaller size. This sacrifices performance, but saves a ton of space. The performance also does not decrease that much. We saved over 10x space and lost significant, but not a ton of performance.  
### 3. Relative Performance for more vs. Fewer images per run, and why
I do not believe we have the data in the provided perf run to answer this question. We only have one run.
### 4. Pipeline stalls waiting for memory

### 5. L2 Invalidations (overwrites of memory)
### 6. LLC Loads and Misses

## Documentation
We used chatGPT to help us figure out how to connect a webcam. It told us to cycle through the initialization (0-12ish) which we did and eventually found that our webcam was floating around in the 7-10 range depending on the time. We used GeeksForGeeks camera debugging code to try and get ours to work. Some of their code residuals are still left in our code. 

### People
C1Cs Matthew Westbrook and Alex White

### LLMs
ChatGPT usage for 
