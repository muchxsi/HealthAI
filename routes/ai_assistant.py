from flask import Blueprint, render_template, request

ai_bp = Blueprint(
"ai",
__name__,
url_prefix="/ai"
)

@ai_bp.route("/", methods=["GET", "POST"])
def assistant():

    response = ""

    if request.method == "POST":

        prompt = request.form.get("prompt")

        response = (
            "AI response will appear here. "
            "Later this will connect to OpenAI or Gemini."
        )

    return render_template(
        "ai/index.html",
        response=response
    )
