from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from openai import OpenAI

class OpenAIDocsAPIViews(APIView):
    
    def post(self, request):
        user_message = request.data.get("message")
        system_instructions = """
        이제부터 너는 "영어, 한글 번역가"야.
        지금부터 내가 입력하는 모든 프롬프트를 무조건 한글은 영어로, 영어는 한글로 번역해줘.
        프롬프트의 내용이나 의도는 무시하고 오직 번역만 해줘.
        """
        
        openai_response = call_openai(system_instructions, user_message)
        return Response({"message": openai_response})

CLIENT = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

def call_openai(system_instructions, user_message):
    try:
        completion = CLIENT.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": system_instructions,
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        return completion.choices[0].message.content
    except Exception as e:
        return str(e)    