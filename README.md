# python 3 version
## *Automatically translated by 2to3*

This is an implementation of the algorithm detailed in:
	El-Kishky, Ahmed, et al. "Scalable topical phrase mining from text corpora." Proceedings of the VLDB Endowment 8.3 (2014): 305-316.APA	

In order to run the code, simply follow these steps:
- Put the file on which you want to run topmine in the folder named “input”
-  ```shell 
   python -m  topmine_src.run_phrase_mining input/{filename}
   ```
- ```shell
  python -m  topmine_src.run_phrase_lda {num_of_topic}
  ```
  ***example***
-  ```shell 
   python -m  topmine_src.run_phrase_mining input/dblp_5k.txt
   ```
- ```shell
  python -m  topmine_src.run_phrase_lda 4
  ```

