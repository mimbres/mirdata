import music21

from mirdata.datasets import haydn_op20
from tests.test_utils import run_track_tests


def test_track():
    default_trackid = "0"
    data_home = "tests/resources/mir_datasets/haydn_op20"
    dataset = haydn_op20.Dataset(data_home)
    track = dataset.track(default_trackid)

    expected_attributes = {
        "humdrum_annotated_path": "tests/resources/mir_datasets/haydn_op20/op20n1-01.hrm",
        "title": "op20n1-01",
        "track_id": "0",
    }

    expected_property_types = {
        "duration": int,
        "chords": list,
        "roman_numerals": list,
        "keys": list,
        "score": music21.stream.Score,
        "midi_path": str,
    }
    run_track_tests(track, expected_attributes, expected_property_types)


def test_to_jam():
    data_home = "tests/resources/mir_datasets/haydn_op20"
    dataset = haydn_op20.Dataset(data_home)
    track = dataset.track("0")
    jam = track.to_jams()
    assert jam["file_metadata"]["title"] == "op20n1-01", "title does not match expected"
    assert jam["file_metadata"]["duration"] == 0, "duration does not match expected"
    assert (
        jam["sandbox"]["humdrum_annotated_path"]
        == "tests/resources/mir_datasets/haydn_op20/op20n1-01.hrm"
    ), "duration does not match expected"
    assert (
        jam["sandbox"]["midi_path"]
        == "tests/resources/mir_datasets/haydn_op20/op20n1-01.midi"
    ), "duration does not match expected"
    assert isinstance(jam["sandbox"]["chords"], list)
    assert jam["sandbox"]["chords"][0]["time"] == 0
    assert jam["sandbox"]["chords"][0]["chord"] == "Eb-major triad"
    assert isinstance(jam["sandbox"]["key"], list)
    assert jam["sandbox"]["key"][0]["time"] == 0
    assert isinstance(jam["sandbox"]["key"][0]["key"], music21.key.Key)
    assert isinstance(jam["sandbox"]["roman_numerals"], list)
    assert jam["sandbox"]["roman_numerals"][0]["time"] == 0
    assert jam["sandbox"]["roman_numerals"][0]["roman_numeral"] == "I"


def test_load_score():
    path = "tests/resources/mir_datasets/haydn_op20/op20n1-01.hrm"
    score = haydn_op20.load_score(path)
    assert isinstance(score, music21.stream.Score)
    assert len(score.parts) == 4


def test_load_key():
    path = "tests/resources/mir_datasets/haydn_op20/op20n1-01.hrm"
    key = haydn_op20.load_key_music21(path)
    assert isinstance(key, list)
    assert len(key) == 1
    assert key[0]["time"] == 0
    assert key[-1]["time"] == 0
    assert isinstance(key[0]["key"], music21.key.Key)


def test_load_chords():
    path = "tests/resources/mir_datasets/haydn_op20/op20n1-01.hrm"
    chords = haydn_op20.load_chords_music21(path)
    assert isinstance(chords, list)
    assert len(chords) == 1
    assert chords[0]["time"] == 0
    assert chords[-1]["time"] == 0
    assert chords[0]["chord"] == "Eb-major triad"
    assert chords[-1]["chord"] == "Eb-major triad"


def test_load_roman_numerals():
    path = "tests/resources/mir_datasets/haydn_op20/op20n1-01.hrm"
    roman_numerals = haydn_op20.load_roman_numerals(path)
    assert isinstance(roman_numerals, list)
    assert len(roman_numerals) == 1
    assert roman_numerals[0]["time"] == 0
    assert roman_numerals[-1]["time"] == 0
    assert roman_numerals[0]["roman_numeral"] == "I"
    assert roman_numerals[-1]["roman_numeral"] == "I"


def test_load_midi_path():
    path = "tests/resources/mir_datasets/haydn_op20/op20n1-01.hrm"
    midi_path = haydn_op20.load_midi_path(path)
    assert isinstance(midi_path, str)
    assert midi_path == "tests/resources/mir_datasets/haydn_op20/op20n1-01.midi"
