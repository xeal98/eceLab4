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
This discussion reviews the performance of the two models we tested, the LiteRT and Keras models. The LiteRT comes in at a significantly lower size than the Keras model which will have implications that are discussed in later sections. LiteRT makes a better model for the Raspberry Pi to run because of its smaller size, fewer pipeline stalls, and fewer misses in the cache. This makes it run substantially faster than the Keras model which makes it preferred in this case. This model is what allowed us to do live inferencing using a webcam to determine if the image was a cat or dog. 
### 2. Relative Model Sizes
The keras model is roughly 10x larger than the LiteRT model. With the keras model being 27 MB and the LiteRT model being 2.4 MB. This means that the LiteRT model nearly fully fits in the 2MB of L2 CPU Cache and leads to far fewer misses (discussed later in Q4 and Q5). The LiteRT model uses optimizations like quantization or pruning of parameters to get to that smaller size. This sacrifices performance, but saves a ton of space. The performance also does not decrease that much. We saved over 10x space and lost significant, but not a ton of performance.  
### 3. Relative Performance for more vs. Fewer images per run, and why
I do not believe we have the data in the provided perf run to answer this question. We only have one run.
### 4. Pipeline stalls waiting for memory
BLUF: More things stored in easier-to-access storage, fewer stalls. 
We saw 13.8x times fewer pipeline stalls when running the LiteRT model compared to the keras model. This means we were able to fetch things from memory faster on average in the LiteRT model because the model was majority stored in the L2 Cache compared to the long time it takes to fetch data from memory in the keras model. 
### 5. L2 Invalidations (overwrites of memory)
This is the ultimate demonstration of Cache versus RAM speed. We see nearly 70x more invalidations of the L2 cache for keras compared to the much smaller LiteRT model. Since more of the LiteRT model fits directly in the cache, we don't need to overwrite the cache as much. Since RAM is 100+ times slower than the cache, this dramatically saves time. The cache for the keras model has to be overwritten often to store data used often while the LiteRT model can store more of its useful data in the cache always, leading to dramatically fewer cache invalidations. 
### 6. LLC Loads and Misses
LLC (Last Level Cache, L3 in our case) loads and misses are important because they show activity in the last level before having to resort to RAM. Since the keras model has 30-35x higher activity in the LLC, we know that it is likely resorting to using RAM far more than the LiteRT model is. This makes sense because we know that the LiteRT model is 2.4 MB and the L2 cache holds 2 MB over all the cores and the L3 cache holds around 2 MB shared between the cores. This means that the LiteRT model is able to greatly minimize its use of RAM since it has a lot of memory in caches compared to its size. The keras model, being 27 MB, cannot come close to fitting in the caches and must rely on RAM more. 

## Documentation
We used chatGPT to help us figure out how to connect a webcam. It told us to cycle through the initialization (0-12ish) which we did and eventually found that our webcam was floating around in the 7-10 range depending on the time. We used GeeksForGeeks camera debugging code to try and get ours to work. Some of their code residuals are still left in our code. 

### People
C1Cs Matthew Westbrook and Alex White

### LLMs
ChatGPT usage for webcam debugging.
