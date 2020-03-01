# SneakySnakes
code for the ANLP Sneaky Snakes Project

In our project, we use two different methods to generate text summaries. 

*******************************
METHOD 1 : TF-IDF-based
One method is based on calculating the TF-IDF scores. The code revolving around that method can be found in the folder "TF-IDF_textSummarisation".
Please download and unzip the folder. Then run the notebooks 
"scrape_bible_summaries.ipynb",
"King James Bible (66 books) to correct format.ipynb" and
"tfidf_summary_german.ipynb"
(the order of running those three does not matter).

Second, run the notebook "tfidf_summaries_66books.ipynb" and afterwards "compare with goldstandard.ipynb".
The latter notebook contains the evaluation part for our TF-IDF based method. 

In some of the notebooks, we create and fill several txt-files. In case that the cells cannot be executed properly, need too long to run
or if You want to jump to the evaluation part ("compare with goldstandard.ipynb") directly, the files are all stored in an additional folder 
called "backup-files". If You want or need to use them, please adjust the file paths in the "compare with goldstandard.ipynb" notebook.


*******************************
METHOD 2 : seq2seq model
The second method is based on training a sequence-to-sequence (seq2seq) model. In order to run the code for the model, please
download and unzip "seq2seq_abstract_text_summarisation.zip". Then run the notebook: "seq2seq_abstract_text_summarisation.ipynb".





