# FTSEStocks-Quant-NLP

The notebook categorises FTSE ALL share index(ASX) stocks in quartile buckets/ranks based on it relative performance in its ICB (ndustry Classification Benchmark) 
classification. A corpus is created by combining business description of stocks in each quartile rank and subsectors. Key Phrase extraction / topic modelling is applied on documents and Topics/Key phrase is extracted. Entity names were filtered out from documents so that only business activities are used for topic modelling. 



The process is applied on a recent market crash(March) 2020 due to COVID pandemic, which saw  stocks in index dropping by over 60% in most sectors. In lowest performing sectors high rankings stocks where preferred to worst performers. The NLP analysis is undertaken to see topics which were favoured by the investors i.e. Are there any business activities that the market thinks will be relatively lesser affected. 



This data exploration activity if proven successful, can be possibly extended to : 
- Generating periodic market performance narrative
- Factor investigation for a risk management strategy, to protect against market crashes. 

