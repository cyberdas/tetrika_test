from typing import Dict

from flask import Flask, jsonify


app = Flask(__name__)


task = {'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473]}


def appearance(intervals: Dict[str, int]) -> int:
    start_lesson, end_lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']

    first = max(start_lesson, pupil[0], tutor[0])
    last = min(end_lesson, pupil[-1], tutor[-1])

    common = pupil + tutor
    common_s = sorted([[common[i-1], common[i]] for i in range(1, len(common), 2)],
                      key=lambda x: x[1])
    lines = [(first, common_s[0][1])]
    right = 0

    for l, r in common_s:
        if r > last:
            r = last
        if l < right:
            lines.append((l, right))
        elif l < lines[-1][1] and r > lines[-1][1]:
            right = r
        elif l > lines[-1][1]:
            lines.append([l, r])

    counter = 0

    for line in lines:
        counter += line[1] - line[0]
    return counter


@app.route('/api/appearance', methods=['GET'])
def api_appearance():
    return jsonify({'Ответ': appearance(task)})


if __name__ == '__main__':
    app.run(debug=True)
