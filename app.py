import streamlit as st
from music21 import note

st.set_page_config(page_title="Kontrabass Griffbrett", layout="wide")

# -----------------------------
# Grunddaten
# -----------------------------

STRINGS = {
    "G": "G2",
    "D": "D2",
    "A": "A1",
    "E": "E1",
}

STRING_WIDTHS = {
    "G": 3,
    "D": 4,
    "A": 5,
    "E": 6,
}

STRING_PRIORITY = {
    "E": 1,
    "A": 2,
    "D": 3,
    "G": 4,
}

SHARP_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
FLAT_NAMES = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

NOTE_COLORS = {
    0: "#E53935",
    1: "#FB8C00",
    2: "#FDD835",
    3: "#7CB342",
    4: "#43A047",
    5: "#00ACC1",
    6: "#039BE5",
    7: "#1E5AA8",
    8: "#8D6E63",
    9: "#D81B60",
    10: "#8E24AA",
    11: "#455A64",
}

SCALES = {
    "Dur": [0, 2, 4, 5, 7, 9, 11],
    "Natürlich Moll": [0, 2, 3, 5, 7, 8, 10],
    "Dorisch": [0, 2, 3, 5, 7, 9, 10],
    "Phrygisch": [0, 1, 3, 5, 7, 8, 10],
    "Lydisch": [0, 2, 4, 6, 7, 9, 11],
    "Mixolydisch": [0, 2, 4, 5, 7, 9, 10],
    "Lokrisch": [0, 1, 3, 5, 6, 8, 10],
    "Moll-Pentatonik": [0, 3, 5, 7, 10],
    "Dur-Pentatonik": [0, 2, 4, 7, 9],
    "Blues": [0, 3, 5, 6, 7, 10],
}

CHORDS = {
    "Dur": [0, 4, 7],
    "Moll": [0, 3, 7],
    "Dominant 7": [0, 4, 7, 10],
    "Maj7": [0, 4, 7, 11],
    "Moll 7": [0, 3, 7, 10],
    "Vermindert": [0, 3, 6],
    "Halbvermindert": [0, 3, 6, 10],
    "Übermäßig": [0, 4, 8],
}

SHARP_KEYS = ["G", "D", "A", "E", "B", "F#", "C#"]
FLAT_KEYS = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"]

MINOR_SHARP_KEYS = ["E", "B", "F#", "C#", "G#", "D#", "A#"]
MINOR_FLAT_KEYS = ["D", "G", "C", "F", "Bb", "Eb", "Ab"]


# -----------------------------
# Simandl-Fingersatzbibliothek
# Phase 1: Dur, 1 Oktave
# -----------------------------
# Format:
# string = Saite
# fret   = Halbtonposition 0-12
# finger = Simandl-Fingersatz
# shift  = Lagenwechsel farbig markieren

MAJOR_SCALE_FINGERINGS = {
    "G": [
        {"string": "E", "fret": 3, "finger": "2", "shift": False},
        {"string": "A", "fret": 0, "finger": "0", "shift": False},
        {"string": "A", "fret": 2, "finger": "1", "shift": False},
        {"string": "A", "fret": 3, "finger": "2", "shift": False},
        {"string": "D", "fret": 0, "finger": "0", "shift": False},
        {"string": "D", "fret": 2, "finger": "1", "shift": False},
        {"string": "D", "fret": 4, "finger": "4", "shift": False},
        {"string": "G", "fret": 0, "finger": "0", "shift": False},
    ],

    "D": [
        {"string": "D", "fret": 0, "finger": "0", "shift": False},
        {"string": "D", "fret": 2, "finger": "1", "shift": False},
        {"string": "D", "fret": 4, "finger": "4", "shift": False},
        {"string": "G", "fret": 0, "finger": "0", "shift": False},
        {"string": "G", "fret": 2, "finger": "1", "shift": False},
        {"string": "G", "fret": 4, "finger": "4", "shift": False},
        {"string": "G", "fret": 6, "finger": "1", "shift": True},
        {"string": "G", "fret": 7, "finger": "2", "shift": False},
    ],

    "A": [
        {"string": "A", "fret": 0, "finger": "0", "shift": False},
        {"string": "A", "fret": 2, "finger": "1", "shift": False},
        {"string": "A", "fret": 4, "finger": "4", "shift": False},
        {"string": "D", "fret": 0, "finger": "0", "shift": False},
        {"string": "D", "fret": 2, "finger": "1", "shift": False},
        {"string": "D", "fret": 4, "finger": "4", "shift": False},
        {"string": "D", "fret": 6, "finger": "1", "shift": True},
        {"string": "D", "fret": 7, "finger": "2", "shift": False},
    ],

    "E": [
        {"string": "E", "fret": 0, "finger": "0", "shift": False},
        {"string": "E", "fret": 2, "finger": "1", "shift": False},
        {"string": "E", "fret": 4, "finger": "4", "shift": False},
        {"string": "A", "fret": 0, "finger": "0", "shift": False},
        {"string": "A", "fret": 2, "finger": "1", "shift": False},
        {"string": "A", "fret": 4, "finger": "4", "shift": False},
        {"string": "A", "fret": 6, "finger": "1", "shift": True},
        {"string": "A", "fret": 7, "finger": "2", "shift": False},
    ],

    "C": [
        {"string": "A", "fret": 3, "finger": "2", "shift": False},
        {"string": "D", "fret": 0, "finger": "0", "shift": False},
        {"string": "D", "fret": 2, "finger": "1", "shift": False},
        {"string": "D", "fret": 3, "finger": "2", "shift": False},
        {"string": "G", "fret": 0, "finger": "0", "shift": False},
        {"string": "G", "fret": 2, "finger": "1", "shift": False},
        {"string": "G", "fret": 4, "finger": "4", "shift": False},
        {"string": "G", "fret": 5, "finger": "1", "shift": True},
    ],

    "F": [
        {"string": "E", "fret": 1, "finger": "1", "shift": False},
        {"string": "E", "fret": 3, "finger": "4", "shift": False},
        {"string": "A", "fret": 0, "finger": "0", "shift": False},
        {"string": "A", "fret": 1, "finger": "1", "shift": False},
        {"string": "A", "fret": 3, "finger": "4", "shift": False},
        {"string": "D", "fret": 0, "finger": "0", "shift": False},
        {"string": "D", "fret": 2, "finger": "1", "shift": True},
        {"string": "D", "fret": 3, "finger": "2", "shift": False},
    ],

    "Bb": [
        {"string": "A", "fret": 1, "finger": "1", "shift": False},
        {"string": "A", "fret": 3, "finger": "4", "shift": False},
        {"string": "D", "fret": 0, "finger": "0", "shift": False},
        {"string": "D", "fret": 1, "finger": "1", "shift": False},
        {"string": "D", "fret": 3, "finger": "4", "shift": False},
        {"string": "G", "fret": 0, "finger": "0", "shift": False},
        {"string": "G", "fret": 2, "finger": "1", "shift": True},
        {"string": "G", "fret": 3, "finger": "2", "shift": False},
    ],

    "Eb": [
        {"string": "D", "fret": 1, "finger": "1", "shift": False},
        {"string": "D", "fret": 3, "finger": "4", "shift": False},
        {"string": "G", "fret": 0, "finger": "0", "shift": False},
        {"string": "G", "fret": 1, "finger": "1", "shift": False},
        {"string": "G", "fret": 3, "finger": "4", "shift": False},
        {"string": "G", "fret": 5, "finger": "1", "shift": True},
        {"string": "G", "fret": 7, "finger": "4", "shift": False},
        {"string": "G", "fret": 8, "finger": "1", "shift": True},
    ],
}


# Enharmonische Zuordnung: gleiche Griffweise, andere Schreibweise
MAJOR_SCALE_FINGERINGS["F#"] = MAJOR_SCALE_FINGERINGS["Gb"] = [
    {"string": "E", "fret": 2, "finger": "1", "shift": False},
    {"string": "E", "fret": 4, "finger": "4", "shift": False},
    {"string": "A", "fret": 1, "finger": "1", "shift": True},
    {"string": "A", "fret": 2, "finger": "2", "shift": False},
    {"string": "A", "fret": 4, "finger": "4", "shift": False},
    {"string": "D", "fret": 1, "finger": "1", "shift": True},
    {"string": "D", "fret": 3, "finger": "4", "shift": False},
    {"string": "D", "fret": 4, "finger": "1", "shift": True},
]

MAJOR_SCALE_FINGERINGS["B"] = MAJOR_SCALE_FINGERINGS["Cb"] = [
    {"string": "A", "fret": 2, "finger": "1", "shift": False},
    {"string": "A", "fret": 4, "finger": "4", "shift": False},
    {"string": "A", "fret": 6, "finger": "1", "shift": True},
    {"string": "A", "fret": 7, "finger": "2", "shift": False},
    {"string": "D", "fret": 4, "finger": "4", "shift": False},
    {"string": "D", "fret": 6, "finger": "1", "shift": True},
    {"string": "D", "fret": 8, "finger": "4", "shift": False},
    {"string": "D", "fret": 9, "finger": "1", "shift": True},
]

MAJOR_SCALE_FINGERINGS["Db"] = MAJOR_SCALE_FINGERINGS["C#"] = [
    {"string": "A", "fret": 4, "finger": "4", "shift": False},
    {"string": "A", "fret": 6, "finger": "1", "shift": True},
    {"string": "A", "fret": 8, "finger": "4", "shift": False},
    {"string": "D", "fret": 4, "finger": "4", "shift": False},
    {"string": "D", "fret": 6, "finger": "1", "shift": True},
    {"string": "D", "fret": 8, "finger": "4", "shift": False},
    {"string": "G", "fret": 5, "finger": "1", "shift": True},
    {"string": "G", "fret": 6, "finger": "2", "shift": False},
]

MAJOR_SCALE_FINGERINGS["Ab"] = MAJOR_SCALE_FINGERINGS["G#"] = [
    {"string": "E", "fret": 4, "finger": "4", "shift": False},
    {"string": "A", "fret": 1, "finger": "1", "shift": True},
    {"string": "A", "fret": 3, "finger": "4", "shift": False},
    {"string": "D", "fret": 1, "finger": "1", "shift": False},
    {"string": "D", "fret": 3, "finger": "4", "shift": False},
    {"string": "G", "fret": 1, "finger": "1", "shift": False},
    {"string": "G", "fret": 3, "finger": "4", "shift": False},
    {"string": "G", "fret": 8, "finger": "1", "shift": True},
]


# -----------------------------
# Hilfsfunktionen
# -----------------------------

def pitch_class(name):
    return note.Note(name + "4").pitch.pitchClass


def resolve_spelling(spelling_choice, mode, root, selected_type):
    if spelling_choice in ["Kreuz", "B"]:
        return spelling_choice

    if "#" in root:
        return "Kreuz"
    if "b" in root:
        return "B"

    if mode == "Tonleiter":
        if selected_type in ["Dur", "Lydisch", "Mixolydisch", "Dur-Pentatonik"]:
            if root in FLAT_KEYS:
                return "B"
            if root in SHARP_KEYS:
                return "Kreuz"

        if selected_type in ["Natürlich Moll", "Dorisch", "Phrygisch", "Lokrisch", "Moll-Pentatonik", "Blues"]:
            if root in MINOR_FLAT_KEYS:
                return "B"
            if root in MINOR_SHARP_KEYS:
                return "Kreuz"

    if mode == "Akkord":
        if root in FLAT_KEYS:
            return "B"
        if root in SHARP_KEYS:
            return "Kreuz"

    return "Kreuz"


def note_name_from_pitch_class(pc, spelling):
    if spelling == "Kreuz":
        return SHARP_NAMES[pc % 12]
    return FLAT_NAMES[pc % 12]


def get_fret_note(open_note, fret):
    n = note.Note(open_note)
    return n.transpose(fret)


def build_target_pitch_classes(mode, root_pc, selected_type):
    if mode == "Einzelton":
        return [root_pc]
    if mode == "Tonleiter":
        return [(root_pc + interval) % 12 for interval in SCALES[selected_type]]
    return [(root_pc + interval) % 12 for interval in CHORDS[selected_type]]


def get_all_positions():
    positions = []
    for string_name in ["G", "D", "A", "E"]:
        for fret in range(0, 13):
            current_note = get_fret_note(STRINGS[string_name], fret)
            positions.append({
                "string": string_name,
                "fret": fret,
                "pc": current_note.pitch.pitchClass,
                "midi": current_note.pitch.midi,
                "octave": current_note.pitch.octave,
            })
    return positions


def library_for_current_selection(mode, selected_type, root, show_fingerings, number_of_octaves):
    if not show_fingerings:
        return None
    if mode != "Tonleiter":
        return None
    if selected_type != "Dur":
        return None
    if number_of_octaves != 1:
        return None
    return MAJOR_SCALE_FINGERINGS.get(root)


def build_library_map(library):
    if not library:
        return {}

    result = {}
    for item in library:
        result[(item["string"], item["fret"])] = {
            "finger": item["finger"],
            "shift": item["shift"],
        }
    return result


def is_library_active_position(pos, library_map, selected_strings, min_fret, max_fret):
    key = (pos["string"], pos["fret"])
    return (
        key in library_map
        and pos["string"] in selected_strings
        and min_fret <= pos["fret"] <= max_fret
    )


def find_first_root_midi(root_pc, selected_strings, min_fret, max_fret):
    candidates = []
    for pos in get_all_positions():
        if (
            pos["string"] in selected_strings
            and min_fret <= pos["fret"] <= max_fret
            and pos["pc"] == root_pc
        ):
            candidates.append(pos["midi"])
    if not candidates:
        return None
    return min(candidates)


def is_highest_string_version(pos, selected_strings, min_fret, max_fret):
    same_pitch_positions = []
    for other in get_all_positions():
        if (
            other["midi"] == pos["midi"]
            and other["string"] in selected_strings
            and min_fret <= other["fret"] <= max_fret
        ):
            same_pitch_positions.append(other)

    if not same_pitch_positions:
        return True

    best_position = max(
        same_pitch_positions,
        key=lambda p: STRING_PRIORITY[p["string"]]
    )

    return (
        pos["string"] == best_position["string"]
        and pos["fret"] == best_position["fret"]
    )


def is_in_active_musical_range(pos, mode, root_pc, selected_strings, min_fret, max_fret,
                               start_at_root, number_of_octaves, prefer_highest_string,
                               library_map):

    if library_map:
        return is_library_active_position(
            pos=pos,
            library_map=library_map,
            selected_strings=selected_strings,
            min_fret=min_fret,
            max_fret=max_fret,
        )

    if pos["string"] not in selected_strings:
        return False

    if not (min_fret <= pos["fret"] <= max_fret):
        return False

    if prefer_highest_string:
        if not is_highest_string_version(pos, selected_strings, min_fret, max_fret):
            return False

    if mode == "Einzelton":
        return True

    if not start_at_root:
        return True

    first_root_midi = find_first_root_midi(root_pc, selected_strings, min_fret, max_fret)

    if first_root_midi is None:
        return False

    upper_limit = first_root_midi + (12 * number_of_octaves)
    return first_root_midi <= pos["midi"] <= upper_limit


def octave_style(octave):
    if octave <= 1:
        return "brightness(75%)"
    if octave == 2:
        return "brightness(100%)"
    return "brightness(130%)"


# -----------------------------
# Griffbrett zeichnen
# -----------------------------

def draw_fretboard(target_pcs, root_pc, mode, spelling, min_fret, max_fret,
                   selected_strings, start_at_root, number_of_octaves,
                   prefer_highest_string, show_fingerings, library):

    library_map = build_library_map(library)

    html = """
    <style>
    .fretboard-wrapper {
        width: 100%;
        overflow-x: auto;
        padding-top: 10px;
    }
    .fretboard {
        width: 100%;
        border-collapse: collapse;
        table-layout: fixed;
        font-family: Arial, sans-serif;
    }
    .fretboard th {
        text-align: center;
        padding: 6px;
        font-size: 14px;
        color: #444;
    }
    .fretboard td {
        height: 72px;
        text-align: center;
        vertical-align: middle;
        position: relative;
        border: none;
    }
    .string-label {
        width: 55px;
        font-weight: bold;
        font-size: 18px;
    }
    .position-line {
        position: absolute;
        left: 50%;
        top: 0;
        bottom: 0;
        width: 1px;
        background: #d0d0d0;
        z-index: 0;
    }
    .string-line {
        position: absolute;
        left: 0;
        right: 0;
        top: 50%;
        transform: translateY(-50%);
        background: #555;
        z-index: 1;
    }
    .inactive-area {
        background: #f3f3f3;
        opacity: 0.45;
    }
    .inactive-string {
        opacity: 0.28;
        filter: grayscale(100%);
    }
    .note-wrap {
        position: relative;
        display: inline-block;
        z-index: 3;
    }
    .note-dot {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 42px;
        height: 42px;
        border-radius: 50%;
        color: white;
        font-weight: bold;
        font-size: 13px;
        box-sizing: border-box;
        box-shadow: 0 1px 4px rgba(0,0,0,0.25);
    }
    .root {
        border: 4px solid black;
    }
    .ghost-dot {
        background: #bdbdbd !important;
        color: #555;
        box-shadow: none;
        opacity: 0.55;
        filter: grayscale(100%) !important;
    }
    .finger-label {
        position: absolute;
        top: -11px;
        right: -15px;
        font-size: 12px;
        font-weight: bold;
        color: #1f1f1f;
        background: rgba(255,255,255,0.92);
        border-radius: 10px;
        padding: 1px 5px;
        line-height: 1.1;
        box-shadow: 0 1px 2px rgba(0,0,0,0.12);
        z-index: 4;
    }
    .finger-shift {
        color: #d35400;
        border: 1px solid #d35400;
    }
    .empty {
        color: #aaa;
        position: relative;
        z-index: 2;
    }
    </style>
    """

    html += "<div class='fretboard-wrapper'>"
    html += "<table class='fretboard'>"

    html += "<tr><th></th>"
    for fret in range(0, 13):
        html += f"<th>{fret}</th>"
    html += "</tr>"

    for string_name in ["G", "D", "A", "E"]:
        string_active = string_name in selected_strings
        row_class = "" if string_active else "inactive-string"

        html += f"<tr class='{row_class}'><td class='string-label'>{string_name}</td>"

        for fret in range(0, 13):
            active_area = min_fret <= fret <= max_fret
            cell_class = "" if active_area else "inactive-area"

            current_note = get_fret_note(STRINGS[string_name], fret)
            pc = current_note.pitch.pitchClass
            octave = current_note.pitch.octave
            midi = current_note.pitch.midi

            pos = {
                "string": string_name,
                "fret": fret,
                "pc": pc,
                "midi": midi,
                "octave": octave,
            }

            line_height = STRING_WIDTHS[string_name]

            html += f"<td class='{cell_class}'>"
            html += "<div class='position-line'></div>"
            html += f"<div class='string-line' style='height:{line_height}px;'></div>"

            if pc in target_pcs:
                display_name = note_name_from_pitch_class(pc, spelling) + str(octave)
                color = NOTE_COLORS[pc]
                brightness = octave_style(octave)

                is_root = pc == root_pc
                is_active = is_in_active_musical_range(
                    pos=pos,
                    mode=mode,
                    root_pc=root_pc,
                    selected_strings=selected_strings,
                    min_fret=min_fret,
                    max_fret=max_fret,
                    start_at_root=start_at_root,
                    number_of_octaves=number_of_octaves,
                    prefer_highest_string=prefer_highest_string,
                    library_map=library_map,
                )

                classes = "note-dot"
                if is_root:
                    classes += " root"
                if not is_active:
                    classes += " ghost-dot"

                html += "<div class='note-wrap'>"
                html += (
                    f"<div class='{classes}' "
                    f"style='background:{color}; filter:{brightness};'>"
                    f"{display_name}</div>"
                )

                key = (string_name, fret)
                if show_fingerings and is_active and key in library_map:
                    finger_info = library_map[key]
                    finger_class = "finger-label"
                    if finger_info["shift"]:
                        finger_class += " finger-shift"
                    html += f"<div class='{finger_class}'>{finger_info['finger']}</div>"

                html += "</div>"
            else:
                html += "<span class='empty'>·</span>"

            html += "</td>"

        html += "</tr>"

    html += "</table>"
    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)


# -----------------------------
# Oberfläche
# -----------------------------

st.title("Kontrabass-Griffbrett")

mode = st.sidebar.selectbox(
    "Modus",
    ["Einzelton", "Tonleiter", "Akkord"]
)

root = st.sidebar.selectbox(
    "Grundton",
    ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"]
)

spelling_choice = st.sidebar.radio(
    "Notennamen anzeigen als",
    ["Automatisch", "Kreuz", "B"]
)

if mode == "Tonleiter":
    selected_type = st.sidebar.selectbox("Tonleiter", list(SCALES.keys()))
elif mode == "Akkord":
    selected_type = st.sidebar.selectbox("Akkord", list(CHORDS.keys()))
else:
    selected_type = None

spelling = resolve_spelling(spelling_choice, mode, root, selected_type)

min_fret, max_fret = st.sidebar.slider(
    "Aktiver Griffbrettbereich",
    0, 12, (0, 12)
)

selected_strings = st.sidebar.multiselect(
    "Saiten",
    ["G", "D", "A", "E"],
    default=["G", "D", "A", "E"]
)

prefer_highest_string = st.sidebar.checkbox(
    "Dupletten nur auf höchster möglicher Saite aktiv anzeigen",
    value=False
)

show_fingerings = st.sidebar.checkbox(
    "Simandl-Fingersätze anzeigen",
    value=False
)

if mode in ["Tonleiter", "Akkord"]:
    start_at_root = st.sidebar.checkbox(
        "Erst ab erstem Grundton aktiv anzeigen",
        value=False
    )

    number_of_octaves = st.sidebar.selectbox(
        "Aktiver Umfang",
        [1, 2, 3],
        index=0,
        format_func=lambda x: f"{x} Oktave" if x == 1 else f"{x} Oktaven"
    )
else:
    start_at_root = False
    number_of_octaves = 1

root_pc = pitch_class(root)
target_pcs = build_target_pitch_classes(mode, root_pc, selected_type)

library = library_for_current_selection(
    mode=mode,
    selected_type=selected_type,
    root=root,
    show_fingerings=show_fingerings,
    number_of_octaves=number_of_octaves,
)

st.subheader("Griffbrett 0–12")

if spelling_choice == "Automatisch":
    st.caption(f"Automatische Notenschreibweise: **{spelling}**")

if show_fingerings and mode == "Tonleiter" and selected_type == "Dur":
    if library:
        st.info("Simandl-Fingersatzbibliothek aktiv: Dur, 1 Oktave.")
    else:
        st.warning("Für diese Auswahl ist noch kein kuratierter Simandl-Fingersatz hinterlegt.")

draw_fretboard(
    target_pcs=target_pcs,
    root_pc=root_pc,
    mode=mode,
    spelling=spelling,
    min_fret=min_fret,
    max_fret=max_fret,
    selected_strings=selected_strings,
    start_at_root=start_at_root,
    number_of_octaves=number_of_octaves,
    prefer_highest_string=prefer_highest_string,
    show_fingerings=show_fingerings,
    library=library,
)

st.caption(
    "Farbe = Tonklasse. Oktavzahl steht im Punkt. "
    "Helligkeit = Oktavlage. Grundton = schwarzer Rand. "
    "Orange Fingersatzzahl = Lagenwechsel. "
    "Bei aktivierter Simandl-Bibliothek sind die kuratierten Griffstellen farbig; andere mögliche Skalentöne bleiben grau."
)