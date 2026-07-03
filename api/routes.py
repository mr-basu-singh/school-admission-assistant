from fastapi import APIRouter

from api.models import QuestionRequest
from services.admission_service import ask_school_assistant

router = APIRouter()


@router.post("/ask")
def ask(request: QuestionRequest):

    return ask_school_assistant(request.question)