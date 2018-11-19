from flask import Blueprint

from rmatics.view.problem.problem import SubmitApi, TrustedSubmitApi, ProblemApi, ProblemSubmissionsFilterApi, \
    problem_runs
from rmatics.view.problem.run import SourceApi

problem_blueprint = Blueprint('problem', __name__, url_prefix='/problem')

problem_blueprint.add_url_rule('/<int:problem_id>/submit_v2', methods=('POST', ),
                               view_func=SubmitApi.as_view('submit'))

problem_blueprint.add_url_rule('/trusted/<int:problem_id>/submit_v2', methods=('POST', ),
                               view_func=TrustedSubmitApi.as_view('trusted_submit'))

problem_blueprint.add_url_rule('/<int:problem_id>', methods=('GET', ),
                               view_func=ProblemApi.as_view('problem'))

problem_blueprint.add_url_rule('/<int:problem_id>/submissions/', methods=('GET', ),
                               view_func=ProblemSubmissionsFilterApi.as_view('problem_submissions'))

problem_blueprint.add_url_rule('/<int:problem_id>/runs', view_func=problem_runs)

problem_blueprint.add_url_rule('/run/<int:run_id>source', methods=('GET', ),
                               view_func=SourceApi.as_view('run_source'))