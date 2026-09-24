import sys

import pytest

import caesar as caesar


class TrackedText(str):
    """A str that remembers whether upper() was called"""
    upper_called = False

    def upper(self):
        TrackedText.upper_called = True
        return str.upper(self)


def run_program(monkeypatch, capsys, plaintext, key):
    """
    runs the program with the given inputs
    :return: the output without line breaks
    """
    TrackedText.upper_called = False
    inputs = iter([TrackedText(plaintext), key])
    monkeypatch.setattr('builtins.input', lambda *args: next(inputs))
    caesar.encrypt()
    return capsys.readouterr().out.replace('\n', '')


def test_A(find_step, monkeypatch, capsys):
    output = run_program(monkeypatch, capsys, 'Hallo', '3')
    if find_step >= 4:
        assert output == 'KDOOR'
    elif find_step >= 2:
        assert output == 'HALLO'
    else:
        assert TrackedText.upper_called, 'Der Klartext wurde nicht in Grossbuchstaben umgewandelt'
        assert output == ''


def test_B(find_step, monkeypatch, capsys):
    output = run_program(monkeypatch, capsys, 'Hallo Welt', '5')
    if find_step == 5:
        assert output == 'MFQQTBJQY'
    elif find_step == 4:
        assert output == 'MFQQT\\JQY'
    elif find_step == 3:
        assert output == 'HALLOWELT'
    elif find_step == 2:
        assert output == 'HALLO WELT'
    else:
        assert TrackedText.upper_called, 'Der Klartext wurde nicht in Grossbuchstaben umgewandelt'
        assert output == ''


def test_C(find_step, monkeypatch, capsys):
    if find_step < 2:
        pytest.skip('Skipping this test for step 1')
    output = run_program(monkeypatch, capsys, 'Caesar ist tot', '10')
    if find_step == 5:
        assert output == 'MKOCKBSCDDYD'
    elif find_step == 4:
        assert output == 'MKO]K\\S]^^Y^'
    elif find_step == 3:
        assert output == 'CAESARISTTOT'
    else:
        assert output == 'CAESAR IST TOT'


def test_D(find_step, monkeypatch, capsys):
    if find_step < 3:
        pytest.skip('Skipping this test for step 1-2')
    output = run_program(monkeypatch, capsys, 'XYZ', '1')
    if find_step == 5:
        assert output == 'YZA'
    elif find_step == 4:
        assert output == 'YZ['
    else:
        assert output == 'XYZ'


def test_E(find_step, monkeypatch, capsys):
    if find_step < 4:
        pytest.skip('Skipping this test for step 1-3')
    output = run_program(monkeypatch, capsys, 'zebra', '1')
    if find_step == 5:
        assert output == 'AFCSB'
    else:
        assert output == '[FCSB'


def test_F(find_step, monkeypatch, capsys):
    if find_step < 5:
        pytest.skip('Skipping this test for step 1-4')
    output = run_program(monkeypatch, capsys, 'Veni Vidi Vici', '13')
    assert output == 'IRAVIVQVIVPV'


@pytest.fixture
def find_step(monkeypatch, capsys):
    output = run_program(monkeypatch, capsys, 'xyz ab', '3')
    if output == '' and TrackedText.upper_called:
        step = 1
    elif output == '':
        print('Your program doesn\'t produce any output and doesn\'t convert the text to uppercase. No tests possible',
              file=sys.stderr)
        pytest.exit(
            'Your program doesn\'t produce any output and doesn\'t convert the text to uppercase. No tests possible')
    elif ' ' in output:
        step = 2
    elif 'XYZ' in output.upper():
        step = 3
    elif '[' in output or '\\' in output or ']' in output:
        step = 4
    elif 'ABCDE' in output:
        step = 5
    else:
        print('Cannot determine the step you are working on.', file=sys.stderr)
        step = 5

    print(f'Executing tests for step {step}', file=sys.stderr)
    return step
