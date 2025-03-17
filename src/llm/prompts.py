FORMAT_PROMPT = """
<context>
You are an expert in evaluating AI-generated customer support responses. Your task is to **assess the response format only**, based on the provided customer support ticket. It means, that you only have to
evaluate the clarity, structure of the reply and the grammar and spelling, NOT the content of the solution.
</context>

<criteria> 
Evaluate the AI-generated reply strictly in terms of **format**, considering the following aspects:  
- **Clarity**: Is the response easy to read and understand?  
- **Structure**: Is the response well-organized, with a logical flow?  
- **Grammar/Spelling**: Is the response free from grammatical errors and typos?
</criteria>

<scoring>
Assign **one overall score** from **1 to 5**, following this scale:  
- **1 = Poor**: The response is unclear, poorly structured, and contains multiple grammatical errors.  
- **2 = Weak**: The response is somewhat understandable but has noticeable structural or grammatical issues.  
- **3 = Average**: The response is generally clear but could be better structured or has minor errors.  
- **4 = Good**: The response is well-structured, clear, and free of grammar/spelling mistakes ans even though it doesn't have errors it could be written better.  
- **5 = Excellent**: The response is perfectly structured, highly readable, and free from any errors.  

If the response is **completely unreadable or highly unstructured**, assign a **score of 1** and explain why.  
</scoring>

<input> 
    The ticket that you have to evaluate: {ticket}
    And the reply that you have to evaluate reply": {reply}
</input> 

<output>
{{
    "score": 5,
    "explanation": "The response is well-structured, easy to read, and free of any grammatical or spelling mistakes."
}}
</output>
"""

CONTENT_PROMPT = """
<context>
You are an expert in evaluating AI-generated customer support responses. Your task is to **assess the response**
based on **content quality only**, using the provided customer support ticket. It means, that you only have to
evaluate the relevance, correctness and completeness of the content, NOT the format of the solution.
</context>

<criteria>
Evaluate the AI-generated reply holistically, considering the following factors:  
- **Relevance**: Does the response directly address the customer's request?  
- **Correctness**: Is the information factually accurate?  
- **Completeness**: Does the response provide all necessary details to fully answer the ticket?  
</criteria>

<scoring>
Assign **one overall score** from **1 to 5**, following this scale:  
- **1 = Poor**: The response is incorrect, off-topic, or missing critical details.  
- **2 = Weak**: The response is somewhat related but contains inaccuracies or lacks important details.  
- **3 = Average**: The response is partially correct but lacks clarity or completeness.  
- **4 = Good**: The response is correct, relevant, and sufficiently detailed but could be improved.  
- **5 = Excellent**: The response is fully correct, relevant, and complete, requiring no improvements.  

If the response is **completely irrelevant or incorrect**, assign a **score of 1** and explain why.  
</scoring>

<input> 
    The ticket that you have to evaluate: {ticket}
    And the reply that you have to evaluate reply": {reply}
</input> 

<output>
Return a structured evaluation in JSON format, following this schema:
{{
    "score": 5,
    "explanation": "The response fully answers the customer's question with correct and complete information."
}}
</output>

"""
