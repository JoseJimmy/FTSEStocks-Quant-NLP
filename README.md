# FTSEStocks-Quant-NLP

The notebook categorises FTSE ALL share index(ASX) stocks in quartile buckets/ranks based on it relative performance in its ICB (ndustry Classification Benchmark) 
classification. A corpus is created by combining business description of stocks in each quartile rank and subsector. Key Phrase extraction / topic modelling is 
applied on documents and Topics/Key phrase is extracted. The Entity names are filtered out from documents so that only bussiness activities are used for topic modelling. 

The method above is applied on a recent market crash(March) 2020 due to COVID pandemic, which saw  stocks in index dropping by over 60% in most sectors. In lowest performing sectors high rankings stocks where 
preferred to worst performers. The NLP analysis is undertaken to see topics which are favoured by tyhe investors i.e. Are there any bussiness activities that the market thinks will be relatvitely 
lesser affected. 

This data exploration activity if proven successful can be used on number of use cases such as 
- Renerating periodic market performance
- Factor investigation for a risk managment stratgey , to protect against market crashes. 
