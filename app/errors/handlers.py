from flask import render_template
from app.errors import bp

from app.api.errors import ApiError

# true if json response is preferred
def wants_json_response():
    return request.accept_mimetypes['application/json'] >= \
        request.accept_mimetypes['text/html']

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/error.html'), 400


@bp.app_errorhandler(ApiError)
def api_error(ApiError):
    # Error raised in API
    if wants_json_response():
        return ApiError.to_response()
    
    return render_template('errors/api_error.html', Error=ApiError), ApiError.status_code