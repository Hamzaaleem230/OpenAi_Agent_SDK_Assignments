from pydantic import BaseModel

class MathHomeworkOutput(BaseModel):
    is_math_homework_query: bool
    reasoning: str
    
class AvoidPoliticalTopicsAndReferenceOutput(BaseModel):
    is_avoid_political_topics_and_reference_query: bool
    reasoning: str
