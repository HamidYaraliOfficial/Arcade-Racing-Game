import sys
import math
import random
import time
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QStackedWidget, QComboBox, QSlider,
    QFrame, QGridLayout, QSizePolicy, QMessageBox, QProgressBar
)
from PyQt6.QtCore import (
    Qt, QTimer, QRect, QPoint, QSize, pyqtSignal, QPropertyAnimation,
    QEasingCurve, QRectF, QPointF
)
from PyQt6.QtGui import (
    QPainter, QColor, QPen, QBrush, QFont, QFontMetrics, QLinearGradient,
    QRadialGradient, QPainterPath, QTransform, QPolygonF, QPalette
)


CAR_COLORS = ["red", "blue", "green", "yellow"]

# ── Data ──────────────────────────────────────────────────
CARS = {
    "red":    {"icon": "🔴", "color": "red",    "name": "Red Racer",    "speed": 5, "accel": 0.4},
    "blue":   {"icon": "🔵", "color": "blue",   "name": "Blue Bolt",    "speed": 6, "accel": 0.3},
    "green":  {"icon": "🟢", "color": "green",  "name": "Green Ghost",  "speed": 4, "accel": 0.5},
    "yellow": {"icon": "🟡", "color": "yellow", "name": "Yellow Flash", "speed": 5, "accel": 0.4},
}

TRACKS = {
    "city":   {"icon": "🏙️", "name": "City",   "length": 1000, "difficulty": 1},
    "desert": {"icon": "🏜️", "name": "Desert", "length": 1200, "difficulty": 2},
    "snow":   {"icon": "🏔️", "name": "Snow",   "length": 800,  "difficulty": 3},
}

DIFFICULTIES = {
    "easy":   {"icon": "🟢", "name": "Easy"},
    "medium": {"icon": "🟡", "name": "Medium"},
    "hard":   {"icon": "🔴", "name": "Hard"},
}





# ─────────────────────────── THEMES ───────────────────────────
TH = {
    "dark": {
        "bg": "#0a0a0f",
        "bg2": "#12121a",
        "card": "#1a1a2e",
        "card2": "#16213e",
        "accent": "#e94560",
        "accent2": "#0f3460",
        "accent3": "#533483",
        "text": "#eaeaea",
        "text2": "#a0a0b0",
        "btn": "#e94560",
        "btn_hover": "#ff6b6b",
        "btn_text": "#ffffff",
        "border": "#2a2a4a",
        "track": "#1a2a1a",
        "road": "#2a2a3a",
        "grass": "#0d1f0d",
        "sky_top": "#050510",
        "sky_bot": "#0a0a20",
        "hud_bg": "rgba(10,10,20,180)",
        "speed_col": "#e94560",
        "lap_col": "#00ff88",
        "nitro_col": "#00aaff",
    },
    "light": {
        "bg": "#f0f0f8",
        "bg2": "#e0e0f0",
        "card": "#ffffff",
        "card2": "#f5f5ff",
        "accent": "#c0392b",
        "accent2": "#2980b9",
        "accent3": "#8e44ad",
        "text": "#1a1a2e",
        "text2": "#4a4a6a",
        "btn": "#c0392b",
        "btn_hover": "#e74c3c",
        "btn_text": "#ffffff",
        "border": "#c0c0d8",
        "track": "#d0e8d0",
        "road": "#9a9aaa",
        "grass": "#a8d8a8",
        "sky_top": "#87ceeb",
        "sky_bot": "#c8e8ff",
        "hud_bg": "rgba(240,240,248,200)",
        "speed_col": "#c0392b",
        "lap_col": "#27ae60",
        "nitro_col": "#2980b9",
    }
}

TR = {
    "en": {
        "title": "Arcade Racing",
        "play": "PLAY",
        "settings": "SETTINGS",
        "exit": "EXIT",
        "back": "BACK",
        "theme": "Theme",
        "language": "Language",
        "dark": "Dark",
        "light": "Light",
        "speed": "SPEED",
        "lap": "LAP",
        "pos": "POS",
        "time": "TIME",
        "nitro": "NITRO",
        "best": "BEST",
        "pause": "PAUSE",
        "resume": "RESUME",
        "restart": "RESTART",
        "menu": "MENU",
        "paused": "PAUSED",
        "race_over": "RACE OVER!",
        "your_time": "Your Time",
        "best_time": "Best Time",
        "laps": "Laps",
        "choose_car": "Choose Car",
        "choose_track": "Choose Track",
        "easy": "Easy",
        "medium": "Medium",
        "hard": "Hard",
        "difficulty": "Difficulty",
        "start_race": "START RACE",
        "controls": "Controls",
        "accel": "Accelerate",
        "brake": "Brake",
        "left": "Turn Left",
        "right": "Turn Right",
        "nitro_key": "Nitro Boost",
        "w_up": "W / ↑",
        "s_down": "S / ↓",
        "a_left": "A / ←",
        "d_right": "D / →",
        "space_nitro": "SPACE",
        "car_red": "Red Racer",
        "car_blue": "Blue Bolt",
        "car_green": "Green Ghost",
        "car_yellow": "Yellow Flash",
        "track_city": "City Circuit",
        "track_desert": "Desert Storm",
        "track_snow": "Arctic Run",
        "finish": "FINISH!",
        "race_complete": "Race Complete!",
        "total_laps": "Total Laps: 3",
        "volume": "Volume",
        "new_record": "NEW RECORD!",
    },
    "fa": {
        "title": "مسابقه آرکید",
        "play": "بازی",
        "settings": "تنظیمات",
        "exit": "خروج",
        "back": "بازگشت",
        "theme": "تم",
        "language": "زبان",
        "dark": "تاریک",
        "light": "روشن",
        "speed": "سرعت",
        "lap": "دور",
        "pos": "رتبه",
        "time": "زمان",
        "nitro": "نیترو",
        "best": "بهترین",
        "pause": "توقف",
        "resume": "ادامه",
        "restart": "شروع مجدد",
        "menu": "منو",
        "paused": "متوقف شد",
        "race_over": "پایان مسابقه!",
        "your_time": "زمان شما",
        "best_time": "بهترین زمان",
        "laps": "دورها",
        "choose_car": "انتخاب ماشین",
        "choose_track": "انتخاب مسیر",
        "easy": "آسان",
        "medium": "متوسط",
        "hard": "سخت",
        "difficulty": "سختی",
        "start_race": "شروع مسابقه",
        "controls": "کنترل‌ها",
        "accel": "شتاب",
        "brake": "ترمز",
        "left": "چرخش چپ",
        "right": "چرخش راست",
        "nitro_key": "نیترو",
        "w_up": "W / ↑",
        "s_down": "S / ↓",
        "a_left": "A / ←",
        "d_right": "D / →",
        "space_nitro": "SPACE",
        "car_red": "مسابق قرمز",
        "car_blue": "برق آبی",
        "car_green": "روح سبز",
        "car_yellow": "برق زرد",
        "track_city": "مدار شهر",
        "track_desert": "طوفان بیابان",
        "track_snow": "مسیر قطبی",
        "finish": "پایان!",
        "race_complete": "مسابقه تمام شد!",
        "total_laps": "مجموع دورها: ۳",
        "volume": "صدا",
        "new_record": "رکورد جدید!",
    },
    "zh": {
        "title": "街机赛车",
        "play": "开始游戏",
        "settings": "设置",
        "exit": "退出",
        "back": "返回",
        "theme": "主题",
        "language": "语言",
        "dark": "深色",
        "light": "浅色",
        "speed": "速度",
        "lap": "圈数",
        "pos": "名次",
        "time": "时间",
        "nitro": "氮气",
        "best": "最佳",
        "pause": "暂停",
        "resume": "继续",
        "restart": "重新开始",
        "menu": "菜单",
        "paused": "已暂停",
        "race_over": "比赛结束！",
        "your_time": "你的时间",
        "best_time": "最佳时间",
        "laps": "圈数",
        "choose_car": "选择赛车",
        "choose_track": "选择赛道",
        "easy": "简单",
        "medium": "中等",
        "hard": "困难",
        "difficulty": "难度",
        "start_race": "开始比赛",
        "controls": "控制",
        "accel": "加速",
        "brake": "刹车",
        "left": "左转",
        "right": "右转",
        "nitro_key": "氮气加速",
        "w_up": "W / ↑",
        "s_down": "S / ↓",
        "a_left": "A / ←",
        "d_right": "D / →",
        "space_nitro": "空格键",
        "car_red": "红色赛车",
        "car_blue": "蓝色闪电",
        "car_green": "绿色幽灵",
        "car_yellow": "黄色闪光",
        "track_city": "城市赛道",
        "track_desert": "沙漠风暴",
        "track_snow": "北极之旅",
        "finish": "完成！",
        "race_complete": "比赛完成！",
        "total_laps": "总圈数：3",
        "volume": "音量",
        "new_record": "新纪录！",
    }
}

CAR_COLORS = {
    "red":    {"body": "#e94560", "roof": "#c0392b", "wheel": "#1a1a2e", "window": "#aaddff"},
    "blue":   {"body": "#0080ff", "roof": "#0050cc", "wheel": "#1a1a2e", "window": "#aaddff"},
    "green":  {"body": "#00c853", "roof": "#007a32", "wheel": "#1a1a2e", "window": "#aaddff"},
    "yellow": {"body": "#ffd600", "roof": "#f9a825", "wheel": "#1a1a2e", "window": "#aaddff"},
}

TRACK_COLORS = {
    "city":   {"road": "#555566", "grass": "#2d4a2d", "barrier": "#e94560", "sky": "#0a0a20"},
    "desert": {"road": "#c8a878", "grass": "#d4a052", "barrier": "#e8c060", "sky": "#2a1a0a"},
    "snow":   {"road": "#ddeeff", "grass": "#c8ddf0", "barrier": "#aaccee", "sky": "#a0b8cc"},
}

# ─────────────────────────── TRACK DEFINITION ───────────────────────────
class TrackSegment:
    def __init__(self, length=200, curve=0.0, hill=0.0):
        self.length = length
        self.curve = curve
        self.hill = hill

def build_track(track_id):
    segs = []
    if track_id == "city":
        pattern = [
            (300, 0.0, 0.0), (200, 2.0, 0.0), (200, 0.0, 0.0),
            (200, -2.0, 0.0), (300, 0.0, 1.0), (200, 3.0, 0.0),
            (200, 0.0, -1.0), (200, -3.0, 0.0), (300, 0.0, 0.0),
            (200, 2.5, 0.5), (200, 0.0, 0.0), (200, -2.5, -0.5),
        ]
    elif track_id == "desert":
        pattern = [
            (400, 0.0, 0.0), (300, 1.5, 0.0), (300, 0.0, 2.0),
            (300, -1.5, -2.0), (400, 0.0, 0.0), (300, 2.0, 1.0),
            (200, 0.0, 0.0), (300, -2.0, -1.0),
        ]
    else:  # snow
        pattern = [
            (250, 0.0, 1.0), (250, 2.0, -1.0), (250, 0.0, 1.5),
            (250, -2.0, -1.5), (250, 0.0, 0.0), (300, 1.5, 1.0),
            (250, 0.0, -1.0), (300, -1.5, 0.0),
        ]
    for p in pattern:
        segs.append(TrackSegment(p[0], p[1], p[2]))
    return segs

# ─────────────────────────── PSEUDO-3D RENDERER ───────────────────────────
class RacingRenderer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.theme = "dark"
        self.lang = "en"
        self.track_id = "city"
        self.car_color = "red"
        self.difficulty = "medium"

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self._init_game()

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._update)
        self._timer.setInterval(16)

        self._keys = set()
        self._paused = False
        self._game_over = False
        self._flash_timer = 0
        self._particles = []
        self._nitro_particles = []
        self._ai_cars = []
        self._best_time = None
        self._new_record = False

    def _init_game(self):
        self.track = build_track(self.track_id)
        self.total_track_len = sum(s.length for s in self.track)

        # Player state
        self.player_pos = 0.0      # position along track
        self.player_x = 0.0       # lateral position (-1 to 1)
        self.player_speed = 0.0
        self.player_angle = 0.0
        self.camera_depth = 0.84
        self.player_lap = 0
        self.race_time = 0.0
        self.race_started = False
        self.race_finished = False
        self.countdown = 3
        self.countdown_timer = 0.0
        self.nitro = 100.0
        self.nitro_active = False
        self.player_pos_rank = 1
        self.segment_index = 0

        diff_mult = {"easy": 0.6, "medium": 1.0, "hard": 1.4}
        self._diff_m = diff_mult.get(self.difficulty, 1.0)
        self.max_speed = 8.0 * self._diff_m
        self.accel_rate = 0.12 * self._diff_m
        self.brake_rate = 0.22
        self.turn_rate = 0.04

        self._setup_ai()

        self.camera_pos = 0.0
        self.draw_dist = 200
        self.road_width = 2000
        self._frame = 0
        self._countdown_shown = True
        self._total_laps = 3

    def _setup_ai(self):
        self._ai_cars = []
        num = {"easy": 2, "medium": 4, "hard": 6}[self.difficulty]
        colors = [c for c in CAR_COLORS if c != self.car_color]
        for i in range(num):
            self._ai_cars.append({
                "pos": random.uniform(-200, 200),
                "x": random.uniform(-0.5, 0.5),
                "speed": random.uniform(3.0, 5.5) * self._diff_m,
                "color": colors[i % len(colors)],
                "lap": 0,
                "target_speed": random.uniform(4.0, 7.0) * self._diff_m,
            })

    def start(self):
        self._init_game()
        self._paused = False
        self._game_over = False
        self._timer.start()
        self.setFocus()

    def stop(self):
        self._timer.stop()

    def pause(self):
        self._paused = True

    def resume(self):
        self._paused = False
        self.setFocus()

    def _update(self):
        if self._paused or self._game_over:
            self.update()
            return

        dt = 0.016
        self._frame += 1

        # Countdown
        if not self.race_started:
            self.countdown_timer += dt
            if self.countdown_timer >= 1.0:
                self.countdown_timer = 0.0
                self.countdown -= 1
                if self.countdown <= 0:
                    self.race_started = True
            self.update()
            return

        self.race_time += dt

        # Input
        accel = Qt.Key.Key_W in self._keys or Qt.Key.Key_Up in self._keys
        brake = Qt.Key.Key_S in self._keys or Qt.Key.Key_Down in self._keys
        left  = Qt.Key.Key_A in self._keys or Qt.Key.Key_Left in self._keys
        right = Qt.Key.Key_D in self._keys or Qt.Key.Key_Right in self._keys
        self.nitro_active = Qt.Key.Key_Space in self._keys and self.nitro > 0

        # Nitro
        if self.nitro_active:
            self.nitro = max(0, self.nitro - 30 * dt)
            if self.nitro <= 0:
                self.nitro_active = False
        else:
            self.nitro = min(100, self.nitro + 8 * dt)

        nitro_mult = 1.5 if self.nitro_active else 1.0

        # Speed
        if accel:
            self.player_speed += self.accel_rate * nitro_mult
        elif brake:
            self.player_speed -= self.brake_rate
        else:
            self.player_speed *= 0.97

        # Current segment curve
        seg = self._get_segment_at(self.player_pos)
        curve = seg.curve if seg else 0.0

        self.player_speed = max(0, min(self.player_speed, self.max_speed * nitro_mult))

        # Steering
        if left:
            self.player_x -= self.turn_rate * (self.player_speed / self.max_speed + 0.3)
        if right:
            self.player_x += self.turn_rate * (self.player_speed / self.max_speed + 0.3)

        # Road drift from curve
        if self.player_speed > 0.1:
            self.player_x -= curve * 0.003 * self.player_speed

        # Off-road friction
        if abs(self.player_x) > 1.0:
            self.player_speed *= 0.96
            self.player_x = max(-2.0, min(2.0, self.player_x))

        # Move
        self.player_pos += self.player_speed
        if self.player_pos >= self.total_track_len:
            self.player_pos -= self.total_track_len
            self.player_lap += 1
            if self.player_lap >= self._total_laps:
                self._finish_race()

        # Camera
        self.camera_pos = self.player_pos

        # AI
        self._update_ai(dt)

        # Particles
        if self.nitro_active and self.player_speed > 1.0:
            for _ in range(3):
                self._nitro_particles.append({
                    "x": random.uniform(-20, 20),
                    "y": random.uniform(0, 10),
                    "vx": random.uniform(-2, 2),
                    "vy": random.uniform(-3, -1),
                    "life": 1.0,
                    "size": random.uniform(4, 10),
                })

        self._nitro_particles = [
            p for p in self._nitro_particles
            if (p.__setitem__("life", p["life"] - 0.08) or True) and p["life"] > 0
        ]

        # Rank
        all_pos = [self.player_pos + self.player_lap * self.total_track_len]
        for ai in self._ai_cars:
            all_pos.append(ai["pos"] + ai["lap"] * self.total_track_len)
        all_pos.sort(reverse=True)
        self.player_pos_rank = all_pos.index(
            self.player_pos + self.player_lap * self.total_track_len
        ) + 1

        self.update()

    def _update_ai(self, dt):
        for ai in self._ai_cars:
            ai["speed"] += (ai["target_speed"] - ai["speed"]) * 0.05
            ai["speed"] = max(0, min(ai["speed"], self.max_speed * 1.1))
            ai["pos"] += ai["speed"]
            if ai["pos"] >= self.total_track_len:
                ai["pos"] -= self.total_track_len
                ai["lap"] += 1
            ai["x"] += random.uniform(-0.01, 0.01)
            ai["x"] = max(-0.8, min(0.8, ai["x"]))

    def _get_segment_at(self, pos):
        p = pos % self.total_track_len
        acc = 0
        for seg in self.track:
            acc += seg.length
            if p < acc:
                return seg
        return self.track[-1]

    def _finish_race(self):
        self.race_finished = True
        self._game_over = True
        if self._best_time is None or self.race_time < self._best_time:
            self._best_time = self.race_time
            self._new_record = True
        else:
            self._new_record = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        w, h = self.width(), self.height()
        tc = TH[self.theme]
        trc = TRACK_COLORS[self.track_id]

        self._draw_sky(painter, w, h, tc, trc)
        self._draw_road(painter, w, h, tc, trc)
        self._draw_hud(painter, w, h, tc)

        if not self.race_started:
            self._draw_countdown(painter, w, h, tc)
        if self._paused:
            self._draw_pause_overlay(painter, w, h, tc)
        if self._game_over:
            self._draw_finish_overlay(painter, w, h, tc)

        painter.end()

    def _draw_sky(self, painter, w, h, tc, trc):
        sky_h = int(h * 0.45)
        grad = QLinearGradient(0, 0, 0, sky_h)
        grad.setColorAt(0, QColor(trc["sky"]))
        grad.setColorAt(1, QColor(trc["sky"]).lighter(150))
        painter.fillRect(0, 0, w, sky_h, grad)

        # Stars / sun
        if self.theme == "dark" or self.track_id in ("city", "desert"):
            random.seed(42)
            for _ in range(80):
                sx = random.randint(0, w)
                sy = random.randint(0, sky_h - 10)
                ss = random.uniform(1, 2.5)
                painter.setPen(Qt.PenStyle.NoPen)
                painter.setBrush(QColor(255, 255, 255, random.randint(100, 220)))
                painter.drawEllipse(QRectF(sx, sy, ss, ss))
            random.seed()
        else:
            # Sun
            sun_x = w * 0.75
            sun_y = sky_h * 0.3
            rg = QRadialGradient(sun_x, sun_y, 50)
            rg.setColorAt(0, QColor(255, 255, 180, 220))
            rg.setColorAt(1, QColor(255, 220, 100, 0))
            painter.setBrush(rg)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(QRectF(sun_x - 50, sun_y - 50, 100, 100))

        # Mountains/buildings silhouette
        self._draw_silhouette(painter, w, sky_h, tc)

    def _draw_silhouette(self, painter, w, sky_h, tc):
        painter.setPen(Qt.PenStyle.NoPen)
        if self.track_id == "city":
            col = QColor(20, 20, 40) if self.theme == "dark" else QColor(80, 80, 120)
            painter.setBrush(col)
            buildings = [
                (0.05, 0.5, 0.08, 0.5), (0.1, 0.35, 0.06, 0.65),
                (0.18, 0.45, 0.07, 0.55), (0.27, 0.3, 0.05, 0.7),
                (0.33, 0.5, 0.08, 0.5), (0.55, 0.4, 0.06, 0.6),
                (0.62, 0.28, 0.07, 0.72), (0.70, 0.45, 0.09, 0.55),
                (0.80, 0.35, 0.06, 0.65), (0.88, 0.48, 0.08, 0.52),
            ]
            for bx, bh, bw, by in buildings:
                x = int(w * bx)
                y = int(sky_h * by)
                bwp = int(w * bw)
                bhp = int(sky_h * bh)
                painter.drawRect(x, y, bwp, sky_h - y)
                # windows
                wc = QColor(255, 255, 100, 80) if self.theme == "dark" else QColor(255, 255, 200, 60)
                painter.setBrush(wc)
                for wy in range(y + 5, sky_h - 10, 10):
                    for wx in range(x + 4, x + bwp - 4, 10):
                        if random.random() > 0.4:
                            painter.drawRect(wx, wy, 4, 5)
                painter.setBrush(col)
        elif self.track_id == "desert":
            col = QColor(80, 40, 10) if self.theme == "dark" else QColor(180, 120, 60)
            painter.setBrush(col)
            path = QPainterPath()
            path.moveTo(0, sky_h)
            pts = [(0.0, 0.85), (0.15, 0.6), (0.25, 0.75), (0.4, 0.5),
                   (0.55, 0.7), (0.7, 0.55), (0.85, 0.72), (1.0, 0.65), (1.0, 1.0)]
            for px, py in pts:
                path.lineTo(w * px, sky_h * py)
            path.closeSubpath()
            painter.drawPath(path)
        else:  # snow
            col = QColor(180, 200, 220) if self.theme == "light" else QColor(60, 80, 100)
            painter.setBrush(col)
            path = QPainterPath()
            path.moveTo(0, sky_h)
            pts = [(0.0, 0.9), (0.1, 0.55), (0.2, 0.7), (0.35, 0.45),
                   (0.5, 0.65), (0.65, 0.5), (0.8, 0.7), (0.9, 0.55), (1.0, 0.8), (1.0, 1.0)]
            for px, py in pts:
                path.lineTo(w * px, sky_h * py)
            path.closeSubpath()
            painter.drawPath(path)
            # Snow caps
            snow = QColor(240, 248, 255, 180)
            painter.setBrush(snow)
            for px, py in [(0.1, 0.55), (0.35, 0.45), (0.65, 0.5)]:
                sx = int(w * px)
                sy = int(sky_h * py)
                path2 = QPainterPath()
                path2.moveTo(sx, sy)
                path2.lineTo(sx - 20, sy + 25)
                path2.lineTo(sx + 20, sy + 25)
                path2.closeSubpath()
                painter.drawPath(path2)

    def _draw_road(self, painter, w, h, tc, trc):
        horizon = int(h * 0.45)
        screen_h = h - horizon

        camera_pos = self.camera_pos
        seg = self._get_segment_at(camera_pos)
        base_curve = seg.curve if seg else 0.0
        base_hill = seg.hill if seg else 0.0

        prev_x1 = 0
        prev_x2 = w
        prev_y = horizon

        x_offset = 0.0
        y_offset = 0.0
        curve_accum = 0.0

        drawn_segs = min(self.draw_dist, 150)

        for i in range(drawn_segs, 0, -1):
            t = i / drawn_segs
            seg_pos = (camera_pos + i * 5) % self.total_track_len
            seg_data = self._get_segment_at(seg_pos)
            curve = seg_data.curve if seg_data else 0.0
            hill = seg_data.hill if seg_data else 0.0

            proj_scale = 1.0 / (t * 2.0 + 0.1)

            y = int(horizon + (0.5 - t) * screen_h * 1.8 - y_offset * proj_scale * 50)
            if y < horizon or y >= h:
                y = max(horizon, min(h - 1, y))

            road_w = int(self.road_width * proj_scale * w / 1000)
            cx = w // 2 + int(x_offset * proj_scale * w * 0.5)

            x1 = cx - road_w
            x2 = cx + road_w

            is_alt = (int(seg_pos / 50) % 2 == 0)

            # Grass
            if i == drawn_segs or y != prev_y:
                grass_col = QColor(trc["grass"])
                if is_alt:
                    grass_col = grass_col.lighter(115)
                painter.fillRect(0, y, w, max(1, prev_y - y), grass_col)

            # Road
            road_col = QColor(trc["road"])
            if is_alt:
                road_col = road_col.lighter(110)
            painter.fillRect(x1, y, x2 - x1, max(1, prev_y - y), road_col)

            # Road edge lines
            edge_w = max(2, road_w // 15)
            painter.fillRect(x1, y, edge_w, max(1, prev_y - y), QColor(trc["barrier"]))
            painter.fillRect(x2 - edge_w, y, edge_w, max(1, prev_y - y), QColor(trc["barrier"]))

            # Center dashes
            if is_alt:
                dash_w = max(2, road_w // 20)
                dash_x = cx - dash_w // 2
                painter.fillRect(dash_x, y, dash_w, max(1, prev_y - y), QColor(255, 255, 255, 180))

            # AI cars
            for ai in self._ai_cars:
                ai_seg_pos = ai["pos"] % self.total_track_len
                if abs(ai_seg_pos - seg_pos) < 10:
                    car_screen_x = cx + int(ai["x"] * road_w * 0.7)
                    car_h = max(8, int(40 * proj_scale * 3))
                    car_w = max(5, int(25 * proj_scale * 3))
                    self._draw_mini_car(painter, car_screen_x, y, car_w, car_h, ai["color"])

            x_offset += curve * 0.8
            y_offset += hill * 0.5
            prev_x1, prev_x2, prev_y = x1, x2, y

        # Player car
        self._draw_player_car(painter, w, h, tc)

        # Nitro particles
        self._draw_nitro_particles(painter, w, h)

    def _draw_mini_car(self, painter, cx, y, cw, ch, color_key):
        colors = CAR_COLORS[color_key]
        # Body
        painter.setBrush(QColor(colors["body"]))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(cx - cw // 2, y - ch, cw, ch)
        # Roof
        painter.setBrush(QColor(colors["roof"]))
        painter.drawRect(cx - cw // 3, y - ch - ch // 3, cw * 2 // 3, ch // 3)
        # Windows
        painter.setBrush(QColor(colors["window"]))
        painter.drawRect(cx - cw // 3 + 1, y - ch - ch // 3 + 1, cw * 2 // 3 - 2, ch // 4)

    def _draw_player_car(self, painter, w, h, tc):
        colors = CAR_COLORS[self.car_color]
        cx = w // 2
        cy = int(h * 0.78)
        cw = max(60, min(120, w // 8))
        ch = int(cw * 0.55)

        # Shadow
        shadow_grad = QRadialGradient(cx, cy + ch // 2, cw)
        shadow_grad.setColorAt(0, QColor(0, 0, 0, 80))
        shadow_grad.setColorAt(1, QColor(0, 0, 0, 0))
        painter.setBrush(shadow_grad)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(cx - cw, cy, cw * 2, ch // 2)

        # Wheels
        wc = QColor(colors["wheel"])
        ww = cw // 5
        wh = cw // 6
        for wx, wy_off in [(-cw // 2, 0), (cw // 2 - ww, 0),
                            (-cw // 2, -ch + wh), (cw // 2 - ww, -ch + wh)]:
            painter.setBrush(wc)
            painter.drawRoundedRect(cx + wx, cy + wy_off - wh, ww, wh * 2, 3, 3)
            # Rim
            painter.setBrush(QColor(180, 180, 200))
            painter.drawEllipse(cx + wx + 2, cy + wy_off - wh + 2, ww - 4, wh * 2 - 4)

        # Body
        body_grad = QLinearGradient(cx - cw // 2, cy - ch, cx - cw // 2, cy)
        body_grad.setColorAt(0, QColor(colors["body"]).lighter(130))
        body_grad.setColorAt(1, QColor(colors["body"]))
        painter.setBrush(body_grad)
        path = QPainterPath()
        path.addRoundedRect(QRectF(cx - cw // 2, cy - ch, cw, ch), 8, 8)
        painter.drawPath(path)

        # Roof
        roof_x = cx - cw // 3
        roof_y = cy - ch - ch // 3
        roof_w = cw * 2 // 3
        roof_h = ch // 3
        painter.setBrush(QColor(colors["roof"]))
        path2 = QPainterPath()
        path2.addRoundedRect(QRectF(roof_x, roof_y, roof_w, roof_h), 5, 5)
        painter.drawPath(path2)

        # Windshield
        painter.setBrush(QColor(colors["window"]))
        painter.setOpacity(0.8)
        wsx = roof_x + 3
        wsy = roof_y + 2
        painter.drawRoundedRect(wsx, wsy, roof_w - 6, roof_h - 4, 3, 3)
        painter.setOpacity(1.0)

        # Headlights
        painter.setBrush(QColor(255, 255, 180))
        hl_y = cy - ch + 5
        painter.drawEllipse(cx - cw // 2 + 3, hl_y, 8, 6)
        painter.drawEllipse(cx + cw // 2 - 11, hl_y, 8, 6)

        # Nitro flame
        if self.nitro_active:
            for side in [-1, 1]:
                flame_x = cx + side * (cw // 4)
                flame_y = cy
                for fi in range(5):
                    alpha = int(200 - fi * 35)
                    size = 6 - fi
                    col = QColor(255, 100 + fi * 20, 0, alpha)
                    painter.setBrush(col)
                    painter.setPen(Qt.PenStyle.NoPen)
                    painter.drawEllipse(
                        flame_x - size // 2,
                        flame_y + fi * 5,
                        size, size + 2
                    )

    def _draw_nitro_particles(self, painter, w, h):
        cx = w // 2
        base_y = int(h * 0.8)
        for p in self._nitro_particles:
            alpha = int(p["life"] * 200)
            col = QColor(0, 150, 255, alpha)
            painter.setBrush(col)
            painter.setPen(Qt.PenStyle.NoPen)
            size = int(p["size"] * p["life"])
            painter.drawEllipse(
                int(cx + p["x"]),
                int(base_y + p["y"]),
                size, size
            )

    def _draw_hud(self, painter, w, h, tc):
        font_sm = QFont("Arial", max(8, w // 80))
        font_md = QFont("Arial", max(10, w // 60), QFont.Weight.Bold)
        font_lg = QFont("Arial", max(14, w // 40), QFont.Weight.Bold)
        tr = TR[self.lang]

        hud_alpha = 200
        painter.setOpacity(0.85)

        # Speed gauge (bottom left)
        gauge_x = int(w * 0.02)
        gauge_y = int(h * 0.72)
        gauge_w = max(100, w // 7)
        gauge_h = int(h * 0.25)

        painter.setBrush(QColor(0, 0, 0, hud_alpha))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(gauge_x, gauge_y, gauge_w, gauge_h, 10, 10)
        painter.setOpacity(1.0)

        # Speed arc
        speed_pct = self.player_speed / self.max_speed
        arc_cx = gauge_x + gauge_w // 2
        arc_cy = gauge_y + gauge_h - 20
        arc_r = min(gauge_w, gauge_h) * 0.4
        arc_rect = QRectF(arc_cx - arc_r, arc_cy - arc_r, arc_r * 2, arc_r * 2)

        painter.setPen(QPen(QColor(60, 60, 80), 3))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawArc(arc_rect, 180 * 16, -180 * 16)

        speed_col = QColor(tc["speed_col"])
        if speed_pct > 0.8:
            speed_col = QColor("#ff4444")
        painter.setPen(QPen(speed_col, 5))
        painter.drawArc(arc_rect, 180 * 16, int(-180 * 16 * speed_pct))

        # Speed number
        speed_kmh = int(self.player_speed * 30)
        painter.setPen(QColor(tc["text"]))
        painter.setFont(font_lg)
        painter.drawText(
            QRect(gauge_x, gauge_y + 5, gauge_w, gauge_h // 2),
            Qt.AlignmentFlag.AlignCenter,
            str(speed_kmh)
        )
        painter.setFont(font_sm)
        painter.drawText(
            QRect(gauge_x, gauge_y + gauge_h // 2 + 5, gauge_w, 20),
            Qt.AlignmentFlag.AlignCenter,
            "km/h"
        )
        painter.setFont(font_sm)
        painter.drawText(
            QRect(gauge_x, gauge_y + gauge_h - 20, gauge_w, 18),
            Qt.AlignmentFlag.AlignCenter,
            tr["speed"]
        )

        # Nitro bar (bottom center-left)
        nitro_x = int(w * 0.3)
        nitro_y = int(h * 0.93)
        nitro_w = int(w * 0.4)
        nitro_h = 14

        painter.setOpacity(0.85)
        painter.setBrush(QColor(0, 0, 0, hud_alpha))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(nitro_x - 5, nitro_y - 5, nitro_w + 10, nitro_h + 18, 6, 6)
        painter.setOpacity(1.0)

        nitro_pct = self.nitro / 100.0
        nitro_fill_col = QColor(0, 180, 255) if not self.nitro_active else QColor(0, 255, 200)
        painter.setBrush(QColor(40, 40, 60))
        painter.drawRoundedRect(nitro_x, nitro_y, nitro_w, nitro_h, 4, 4)
        if nitro_pct > 0:
            grad = QLinearGradient(nitro_x, 0, nitro_x + nitro_w, 0)
            grad.setColorAt(0, nitro_fill_col.darker(120))
            grad.setColorAt(1, nitro_fill_col)
            painter.setBrush(grad)
            painter.drawRoundedRect(nitro_x, nitro_y, int(nitro_w * nitro_pct), nitro_h, 4, 4)

        painter.setFont(font_sm)
        painter.setPen(QColor(tc["text"]))
        painter.drawText(
            QRect(nitro_x, nitro_y + nitro_h + 2, nitro_w, 14),
            Qt.AlignmentFlag.AlignCenter,
            f"⚡ {tr['nitro']} {int(self.nitro)}%"
        )

        # Top info bar
        info_h = max(35, h // 18)
        painter.setOpacity(0.85)
        painter.setBrush(QColor(0, 0, 0, hud_alpha))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(0, 0, w, info_h, 0, 0)
        painter.setOpacity(1.0)

        painter.setFont(font_md)
        painter.setPen(QColor(tc["lap_col"]))
        lap_str = f"{tr['lap']}: {min(self.player_lap + 1, self._total_laps)}/{self._total_laps}"
        painter.drawText(QRect(10, 0, w // 4, info_h), Qt.AlignmentFlag.AlignVCenter, lap_str)

        # Time
        mins = int(self.race_time) // 60
        secs = int(self.race_time) % 60
        ms = int((self.race_time % 1) * 100)
        time_str = f"{tr['time']}: {mins:02d}:{secs:02d}.{ms:02d}"
        painter.setPen(QColor(tc["text"]))
        painter.drawText(QRect(w // 4, 0, w // 2, info_h), Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter, time_str)

        # Position
        pos_str = f"{tr['pos']}: {self.player_pos_rank}/{len(self._ai_cars) + 1}"
        painter.setPen(QColor(tc["nitro_col"]))
        painter.drawText(QRect(w * 3 // 4, 0, w // 4 - 10, info_h), Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter, pos_str)

    def _draw_countdown(self, painter, w, h, tc):
        painter.setOpacity(0.6)
        painter.setBrush(QColor(0, 0, 0))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(0, 0, w, h)
        painter.setOpacity(1.0)

        font = QFont("Arial", max(40, w // 8), QFont.Weight.Bold)
        painter.setFont(font)

        if self.countdown > 0:
            text = str(self.countdown)
            col = QColor("#e94560")
        else:
            text = TR[self.lang].get("play", "GO!")
            col = QColor("#00ff88")

        painter.setPen(col)
        painter.drawText(QRect(0, 0, w, h), Qt.AlignmentFlag.AlignCenter, text)

    def _draw_pause_overlay(self, painter, w, h, tc):
        painter.setOpacity(0.5)
        painter.setBrush(QColor(0, 0, 0))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(0, 0, w, h)
        painter.setOpacity(1.0)

        font = QFont("Arial", max(20, w // 20), QFont.Weight.Bold)
        painter.setFont(font)
        painter.setPen(QColor(tc["text"]))
        painter.drawText(
            QRect(0, h // 3, w, h // 3),
            Qt.AlignmentFlag.AlignCenter,
            TR[self.lang]["paused"]
        )

    def _draw_finish_overlay(self, painter, w, h, tc):
        painter.setOpacity(0.7)
        painter.setBrush(QColor(0, 0, 0))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(0, 0, w, h)
        painter.setOpacity(1.0)

        tr = TR[self.lang]
        box_w = min(400, w - 40)
        box_h = min(300, h - 80)
        box_x = (w - box_w) // 2
        box_y = (h - box_h) // 2

        painter.setBrush(QColor(TH[self.theme]["card"]))
        painter.setPen(QPen(QColor(TH[self.theme]["accent"]), 2))
        painter.drawRoundedRect(box_x, box_y, box_w, box_h, 15, 15)

        font_title = QFont("Arial", max(16, w // 30), QFont.Weight.Bold)
        font_info = QFont("Arial", max(10, w // 55))
        font_rec = QFont("Arial", max(12, w // 40), QFont.Weight.Bold)

        painter.setFont(font_title)
        painter.setPen(QColor(tc["accent"]))
        painter.drawText(
            QRect(box_x, box_y + 15, box_w, 40),
            Qt.AlignmentFlag.AlignCenter,
            tr["race_complete"]
        )

        mins = int(self.race_time) // 60
        secs = int(self.race_time) % 60
        ms = int((self.race_time % 1) * 100)
        time_str = f"{mins:02d}:{secs:02d}.{ms:02d}"

        painter.setFont(font_info)
        painter.setPen(QColor(tc["text"]))
        info_y = box_y + 65

        for label, val in [
            (tr["your_time"], time_str),
            (tr["laps"], f"{self._total_laps}/{self._total_laps}"),
            (tr["pos"], f"{self.player_pos_rank}/{len(self._ai_cars) + 1}"),
        ]:
            painter.drawText(
                QRect(box_x + 20, info_y, box_w // 2 - 10, 28),
                Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter,
                label
            )
            painter.setPen(QColor(tc["lap_col"]))
            painter.drawText(
                QRect(box_x + box_w // 2, info_y, box_w // 2 - 20, 28),
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter,
                val
            )
            painter.setPen(QColor(tc["text"]))
            info_y += 32

        if self._new_record:
            painter.setFont(font_rec)
            painter.setPen(QColor("#ffd700"))
            painter.drawText(
                QRect(box_x, info_y + 5, box_w, 30),
                Qt.AlignmentFlag.AlignCenter,
                f"⭐ {tr['new_record']} ⭐"
            )

    def keyPressEvent(self, event):
        self._keys.add(event.key())
        if event.key() == Qt.Key.Key_Escape:
            self.pause_requested.emit()

    def keyReleaseEvent(self, event):
        self._keys.discard(event.key())

    pause_requested = pyqtSignal()


# ─────────────────────────── PAGES ───────────────────────────
class StyledButton(QPushButton):
    def __init__(self, text, theme, parent=None):
        super().__init__(text, parent)
        self.theme = theme
        self._apply()
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(44)

    def _apply(self):
        tc = TH[self.theme]
        self.setStyleSheet(f"""
            QPushButton {{
                background: qlineargradient(x1:0,y1:0,x2:0,y2:1,
                    stop:0 {tc['btn']}, stop:1 {QColor(tc['btn']).darker(130).name()});
                color: {tc['btn_text']};
                border: 1.5px solid {tc['accent']};
                border-radius: 10px;
                padding: 10px 24px;
                font-size: 14px;
                font-weight: bold;
                letter-spacing: 1px;
            }}
            QPushButton:hover {{
                background: qlineargradient(x1:0,y1:0,x2:0,y2:1,
                    stop:0 {tc['btn_hover']}, stop:1 {tc['btn']});
                border-color: {tc['btn_hover']};
            }}
            QPushButton:pressed {{
                background: {QColor(tc['btn']).darker(150).name()};
            }}
        """)

    def refresh(self):
        self._apply()


class MenuPage(QWidget):
    play_clicked = pyqtSignal()
    settings_clicked = pyqtSignal()
    exit_clicked = pyqtSignal()

    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.lang = lang
        self._build()

    def _build(self):
        self._layout = QVBoxLayout(self)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._layout.setSpacing(0)
        self._items = []
        self._refresh_layout()

    def _refresh_layout(self):
        while self._layout.count():
            item = self._layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        self._items.clear()

        tc = TH[self.theme]
        tr = TR[self.lang]

        self.setStyleSheet(f"""
            QWidget {{
                background: transparent;
            }}
        """)

        # Title
        title = QLabel(tr["title"])
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"""
            color: {tc['accent']};
            font-size: 42px;
            font-weight: bold;
            letter-spacing: 3px;
            margin-bottom: 8px;
        """)
        self._layout.addWidget(title)

        sub = QLabel("⚡ FAST · FURIOUS · FUN ⚡")
        sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub.setStyleSheet(f"color:{tc['text2']}; font-size:13px; margin-bottom:40px;")
        self._layout.addWidget(sub)
        self._layout.addSpacing(30)

        for key, signal in [("play", self.play_clicked), ("settings", self.settings_clicked), ("exit", self.exit_clicked)]:
            btn = StyledButton(tr[key], self.theme)
            btn.setMinimumWidth(220)
            btn.setMinimumHeight(50)
            btn.clicked.connect(signal.emit)
            self._layout.addWidget(btn, 0, Qt.AlignmentFlag.AlignCenter)
            self._layout.addSpacing(12)
            self._items.append(btn)

        self._layout.addSpacing(30)
        ver = QLabel("v1.0.0  |  PyQt6")
        ver.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ver.setStyleSheet(f"color:{tc['text2']}; font-size:10px;")
        self._layout.addWidget(ver)

    def refresh(self):
        self._refresh_layout()


class CarSelectPage(QWidget):
    back_clicked = pyqtSignal()
    start_clicked = pyqtSignal(str, str, str)

    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.lang = lang
        self._sel_car = "red"
        self._sel_track = "city"
        self._sel_diff = "medium"
        self._build()

    def _build(self):
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(20, 20, 20, 20)
        self._main_layout.setSpacing(16)
        self._refresh_layout()

    def _refresh_layout(self):
        while self._main_layout.count():
            item = self._main_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        tc = TH[self.theme]
        tr = TR[self.lang]

        self.setStyleSheet(f"background:transparent; color:{tc['text']};")

        # Title
        title = QLabel(f"🏎️  {tr['choose_car']}")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color:{tc['accent']}; font-size:26px; font-weight:bold; margin-bottom:6px;")
        self._main_layout.addWidget(title)

        # ── Car Selection ──
        car_frame = QFrame()
        car_frame.setStyleSheet(f"""
            QFrame {{
                background:{tc['card']};
                border-radius:14px;
                border:1px solid {tc['border']};
            }}
        """)
        car_v = QVBoxLayout(car_frame)
        car_v.setContentsMargins(16, 14, 16, 14)
        car_v.setSpacing(10)

        car_title = QLabel(f"🚗 {tr['choose_car']}")
        car_title.setStyleSheet(f"color:{tc['accent']}; font-weight:bold; font-size:13px;")
        car_v.addWidget(car_title)

        car_row = QHBoxLayout()
        car_row.setSpacing(10)

        for car_id, car_info in CARS.items():
            card = QFrame()
            is_sel = car_id == self._sel_car
            card.setStyleSheet(f"""
                QFrame {{
                    background:{'rgba(255,255,255,18)' if is_sel else tc['card2']};
                    border-radius:10px;
                    border:{'2px solid ' + tc['accent'] if is_sel else '1px solid ' + tc['border']};
                }}
            """)
            card.setCursor(Qt.CursorShape.PointingHandCursor)
            card.mousePressEvent = lambda e, c=car_id: self._select_car(c)

            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(10, 10, 10, 10)
            card_layout.setSpacing(4)
            card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

            # Car preview (colored rectangle)
            preview = QLabel()
            preview.setFixedSize(60, 36)
            preview.setStyleSheet(f"""
                background:{car_info['color']};
                border-radius:6px;
                border:2px solid {'white' if is_sel else 'rgba(255,255,255,30)'};
            """)
            preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
            card_layout.addWidget(preview, 0, Qt.AlignmentFlag.AlignCenter)

            name_lbl = QLabel(car_info["name"])
            name_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            name_lbl.setStyleSheet(f"color:{tc['text']}; font-size:12px; font-weight:{'bold' if is_sel else 'normal'};")
            card_layout.addWidget(name_lbl)

            speed_lbl = QLabel(f"⚡ {car_info['speed']}")
            speed_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            speed_lbl.setStyleSheet(f"color:{tc['text2']}; font-size:10px;")
            card_layout.addWidget(speed_lbl)

            car_row.addWidget(card)

        car_v.addLayout(car_row)
        self._main_layout.addWidget(car_frame)

        # ── Track Selection ──
        track_frame = QFrame()
        track_frame.setStyleSheet(f"""
            QFrame {{
                background:{tc['card']};
                border-radius:14px;
                border:1px solid {tc['border']};
            }}
        """)
        track_v = QVBoxLayout(track_frame)
        track_v.setContentsMargins(16, 14, 16, 14)
        track_v.setSpacing(10)

        track_title = QLabel(f"🗺️ {tr['choose_track']}")
        track_title.setStyleSheet(f"color:{tc['accent']}; font-weight:bold; font-size:13px;")
        track_v.addWidget(track_title)

        track_row = QHBoxLayout()
        track_row.setSpacing(10)

        for track_id, track_info in TRACKS.items():
            card = QFrame()
            is_sel = track_id == self._sel_track
            card.setStyleSheet(f"""
                QFrame {{
                    background:{'rgba(255,255,255,18)' if is_sel else tc['card2']};
                    border-radius:10px;
                    border:{'2px solid ' + tc['accent'] if is_sel else '1px solid ' + tc['border']};
                }}
            """)
            card.setCursor(Qt.CursorShape.PointingHandCursor)
            card.mousePressEvent = lambda e, t=track_id: self._select_track(t)

            card_layout = QVBoxLayout(card)
            card_layout.setContentsMargins(12, 10, 12, 10)
            card_layout.setSpacing(4)
            card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

            icon_lbl = QLabel(track_info["icon"])
            icon_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            icon_lbl.setStyleSheet("font-size:28px;")
            card_layout.addWidget(icon_lbl)

            name_lbl = QLabel(track_info["name"])
            name_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            name_lbl.setStyleSheet(f"color:{tc['text']}; font-size:12px; font-weight:{'bold' if is_sel else 'normal'};")
            card_layout.addWidget(name_lbl)

            track_row.addWidget(card)

        track_v.addLayout(track_row)
        self._main_layout.addWidget(track_frame)

        # ── Difficulty Selection ──
        diff_frame = QFrame()
        diff_frame.setStyleSheet(f"""
            QFrame {{
                background:{tc['card']};
                border-radius:14px;
                border:1px solid {tc['border']};
            }}
        """)
        diff_v = QVBoxLayout(diff_frame)
        diff_v.setContentsMargins(16, 14, 16, 14)
        diff_v.setSpacing(10)

        diff_title = QLabel(f"🎯 {tr['difficulty']}")
        diff_title.setStyleSheet(f"color:{tc['accent']}; font-weight:bold; font-size:13px;")
        diff_v.addWidget(diff_title)

        diff_row = QHBoxLayout()
        diff_row.setSpacing(10)

        for diff_id, diff_info in DIFFICULTIES.items():
            btn = QPushButton(f"{diff_info['icon']} {diff_info['name']}")
            is_sel = diff_id == self._sel_diff
            btn.setStyleSheet(f"""
                QPushButton {{
                    background:{'rgba(255,255,255,18)' if is_sel else tc['card2']};
                    color:{tc['accent'] if is_sel else tc['text']};
                    border:{'2px solid ' + tc['accent'] if is_sel else '1px solid ' + tc['border']};
                    border-radius:8px;
                    padding:8px 20px;
                    font-size:13px;
                    font-weight:{'bold' if is_sel else 'normal'};
                }}
                QPushButton:hover {{ background: rgba(255,255,255,12); }}
            """)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda checked, d=diff_id: self._select_diff(d))
            diff_row.addWidget(btn)

        diff_v.addLayout(diff_row)
        self._main_layout.addWidget(diff_frame)

        # ── Controls Info ──
        ctrl_frame = QFrame()
        ctrl_frame.setStyleSheet(f"""
            QFrame {{
                background:{tc['card']};
                border-radius:14px;
                border:1px solid {tc['border']};
            }}
        """)
        ctrl_layout = QGridLayout(ctrl_frame)
        ctrl_layout.setContentsMargins(16, 14, 16, 14)
        ctrl_layout.setSpacing(8)

        ctrl_lbl = QLabel(f"🎮 {tr['controls']}")
        ctrl_lbl.setStyleSheet(f"color:{tc['accent']}; font-weight:bold; font-size:13px;")
        ctrl_layout.addWidget(ctrl_lbl, 0, 0, 1, 4)

        controls = [
            (tr["accel"],     tr["w_up"]),
            (tr["brake"],     tr["s_down"]),
            (tr["left"],      tr["a_left"]),
            (tr["right"],     tr["d_right"]),
            (tr["nitro_key"], tr["space_nitro"]),
        ]
        for i, (action, key) in enumerate(controls):
            row = i // 2 + 1
            col = (i % 2) * 2
            al = QLabel(action)
            al.setStyleSheet(f"color:{tc['text2']}; font-size:11px;")
            kl = QLabel(key)
            kl.setStyleSheet(f"""
                color:{tc['text']};
                background:{tc['card2']};
                border:1px solid {tc['border']};
                border-radius:4px;
                padding:2px 6px;
                font-size:11px;
                font-weight:bold;
            """)
            ctrl_layout.addWidget(al, row, col)
            ctrl_layout.addWidget(kl, row, col + 1)

        self._main_layout.addWidget(ctrl_frame)

        # ── Buttons ──
        btn_row = QHBoxLayout()
        btn_row.setSpacing(12)

        back_btn = StyledButton(tr["back"], self.theme)
        back_btn.clicked.connect(self.back_clicked.emit)
        btn_row.addWidget(back_btn)

        start_btn = StyledButton(f"🏁 {tr['start_race']}", self.theme)
        start_btn.setMinimumHeight(52)
        start_btn.clicked.connect(self._on_start)
        btn_row.addWidget(start_btn)

        self._main_layout.addLayout(btn_row)


    def _select_car(self, car_id):
        self._sel_car = car_id
        self._refresh_layout()

    def _select_track(self, track_id):
        self._sel_track = track_id
        self._refresh_layout()

    def _select_diff(self, diff_id):
        self._sel_diff = diff_id
        self._refresh_layout()

    def _on_start(self):
        self.start_clicked.emit(self._sel_car, self._sel_track, self._sel_diff)

    def refresh(self):
        self._refresh_layout()


class SettingsPage(QWidget):
    back_clicked = pyqtSignal()
    theme_changed = pyqtSignal(str)
    lang_changed = pyqtSignal(str)

    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.lang = lang
        self._build()

    def _build(self):
        self._main_layout = QVBoxLayout(self)
        self._main_layout.setContentsMargins(40, 30, 40, 30)
        self._main_layout.setSpacing(20)
        self._main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._refresh_layout()

    def _refresh_layout(self):
        while self._main_layout.count():
            item = self._main_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        tc = TH[self.theme]
        tr = TR[self.lang]

        self.setStyleSheet(f"background:transparent; color:{tc['text']};")

        title = QLabel(f"⚙️  {tr['settings']}")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color:{tc['accent']}; font-size:26px; font-weight:bold; margin-bottom:10px;")
        self._main_layout.addWidget(title)

        # Theme
        theme_card = QFrame()
        theme_card.setStyleSheet(f"""
            QFrame {{
                background:{tc['card']};
                border-radius:14px;
                border:1px solid {tc['border']};
            }}
        """)
        theme_layout = QHBoxLayout(theme_card)
        theme_layout.setContentsMargins(20, 16, 20, 16)
        theme_layout.setSpacing(16)

        theme_icon = QLabel("🎨")
        theme_icon.setStyleSheet("font-size:22px; border:none;")
        theme_layout.addWidget(theme_icon)

        theme_lbl = QLabel(tr["theme"])
        theme_lbl.setStyleSheet(f"color:{tc['text']}; font-size:15px; font-weight:bold; border:none;")
        theme_layout.addWidget(theme_lbl)
        theme_layout.addStretch()

        for t_id, t_name in [("dark", tr["dark"]), ("light", tr["light"])]:
            btn = QPushButton(t_name)
            is_sel = t_id == self.theme
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {'rgba(255,255,255,20)' if is_sel else 'transparent'};
                    color: {tc['accent'] if is_sel else tc['text2']};
                    border: {'2px solid ' + tc['accent'] if is_sel else '1px solid ' + tc['border']};
                    border-radius: 8px;
                    padding: 7px 18px;
                    font-size: 13px;
                    font-weight: {'bold' if is_sel else 'normal'};
                }}
                QPushButton:hover {{ background: rgba(255,255,255,12); }}
            """)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda checked, t=t_id: self.theme_changed.emit(t))
            theme_layout.addWidget(btn)

        self._main_layout.addWidget(theme_card)

        # Language
        lang_card = QFrame()
        lang_card.setStyleSheet(f"""
            QFrame {{
                background:{tc['card']};
                border-radius:14px;
                border:1px solid {tc['border']};
            }}
        """)
        lang_layout = QHBoxLayout(lang_card)
        lang_layout.setContentsMargins(20, 16, 20, 16)
        lang_layout.setSpacing(16)

        lang_icon = QLabel("🌐")
        lang_icon.setStyleSheet("font-size:22px; border:none;")
        lang_layout.addWidget(lang_icon)

        lang_lbl = QLabel(tr["language"])
        lang_lbl.setStyleSheet(f"color:{tc['text']}; font-size:15px; font-weight:bold; border:none;")
        lang_layout.addWidget(lang_lbl)
        lang_layout.addStretch()

        langs = [("en", "English"), ("fa", "فارسی"), ("zh", "中文")]
        for l_id, l_name in langs:
            btn = QPushButton(l_name)
            is_sel = l_id == self.lang
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: {'rgba(255,255,255,20)' if is_sel else 'transparent'};
                    color: {tc['accent'] if is_sel else tc['text2']};
                    border: {'2px solid ' + tc['accent'] if is_sel else '1px solid ' + tc['border']};
                    border-radius: 8px;
                    padding: 7px 16px;
                    font-size: 13px;
                    font-weight: {'bold' if is_sel else 'normal'};
                }}
                QPushButton:hover {{ background: rgba(255,255,255,12); }}
            """)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda checked, l=l_id: self.lang_changed.emit(l))
            lang_layout.addWidget(btn)

        self._main_layout.addWidget(lang_card)

        # Info card
        info_card = QFrame()
        info_card.setStyleSheet(f"""
            QFrame {{
                background:{tc['card2']};
                border-radius:14px;
                border:1px solid {tc['border']};
            }}
        """)
        info_layout = QVBoxLayout(info_card)
        info_layout.setContentsMargins(20, 16, 20, 16)
        info_layout.setSpacing(8)

        for icon, txt in [
            ("🏎️", "Pseudo-3D Racing Engine"),
            ("🌍", "3 Languages · 2 Themes"),
            ("⚡", "Nitro Boost System"),
            ("🤖", "AI Opponents"),
            ("📱", "Fully Responsive UI"),
        ]:
            row = QHBoxLayout()
            il = QLabel(icon)
            il.setStyleSheet("font-size:16px; border:none;")
            tl = QLabel(txt)
            tl.setStyleSheet(f"color:{tc['text2']}; font-size:12px; border:none;")
            row.addWidget(il)
            row.addWidget(tl)
            row.addStretch()
            info_layout.addLayout(row)

        self._main_layout.addWidget(info_card)

        self._main_layout.addStretch()

        back_btn = StyledButton(f"← {tr['back']}", self.theme)
        back_btn.setMinimumWidth(160)
        back_btn.clicked.connect(self.back_clicked.emit)
        self._main_layout.addWidget(back_btn, 0, Qt.AlignmentFlag.AlignCenter)

    def refresh(self):
        self._refresh_layout()


class GamePage(QWidget):
    back_to_menu = pyqtSignal()
    restart_requested = pyqtSignal()

    def __init__(self, theme, lang, parent=None):
        super().__init__(parent)
        self.theme = theme
        self.lang = lang
        self._paused = False
        self._build()

    def _build(self):
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self.renderer = RacingRenderer(self)
        self.renderer.pause_requested.connect(self._toggle_pause)
        self._layout.addWidget(self.renderer)

        # Pause/control bar
        self._ctrl_bar = QFrame()
        self._ctrl_bar.setFixedHeight(44)
        self._ctrl_bar.setStyleSheet(f"background:{TH[self.theme]['card']}; border-top:1px solid {TH[self.theme]['border']};")

        ctrl_layout = QHBoxLayout(self._ctrl_bar)
        ctrl_layout.setContentsMargins(10, 4, 10, 4)
        ctrl_layout.setSpacing(8)

        tc = TH[self.theme]
        tr = TR[self.lang]

        btn_style = f"""
            QPushButton {{
                background:{tc['card2']};
                color:{tc['text']};
                border:1px solid {tc['border']};
                border-radius:6px;
                padding:4px 14px;
                font-size:12px;
                font-weight:bold;
            }}
            QPushButton:hover {{
                background:{tc['btn']};
                color:{tc['btn_text']};
            }}
        """

        self._pause_btn = QPushButton(tr["pause"])
        self._pause_btn.setStyleSheet(btn_style)
        self._pause_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self._pause_btn.clicked.connect(self._toggle_pause)
        ctrl_layout.addWidget(self._pause_btn)

        restart_btn = QPushButton(tr["restart"])
        restart_btn.setStyleSheet(btn_style)
        restart_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        restart_btn.clicked.connect(self._do_restart)
        ctrl_layout.addWidget(restart_btn)

        ctrl_layout.addStretch()

        menu_btn = QPushButton(f"⏏ {tr['menu']}")
        menu_btn.setStyleSheet(btn_style)
        menu_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        menu_btn.clicked.connect(self._go_menu)
        ctrl_layout.addWidget(menu_btn)

        self._layout.addWidget(self._ctrl_bar)

    def start_race(self, car_color, track_id, difficulty):
        self.renderer.car_color = car_color
        self.renderer.track_id = track_id
        self.renderer.difficulty = difficulty
        self.renderer.theme = self.theme
        self.renderer.lang = self.lang
        self._paused = False
        self._update_pause_btn()
        self.renderer.start()

    def _toggle_pause(self):
        self._paused = not self._paused
        if self._paused:
            self.renderer.pause()
        else:
            self.renderer.resume()
        self._update_pause_btn()

    def _update_pause_btn(self):
        tr = TR[self.lang]
        self._pause_btn.setText(tr["resume"] if self._paused else tr["pause"])

    def _do_restart(self):
        self._paused = False
        self._update_pause_btn()
        self.restart_requested.emit()

    def _go_menu(self):
        self.renderer.stop()
        self.back_to_menu.emit()

    def refresh(self):
        tc = TH[self.theme]
        tr = TR[self.lang]
        self._ctrl_bar.setStyleSheet(
            f"background:{tc['card']}; border-top:1px solid {tc['border']};"
        )
        self.renderer.theme = self.theme
        self.renderer.lang = self.lang
        self._update_pause_btn()


# ─────────────────────────── BACKGROUND WIDGET ───────────────────────────
class BackgroundWidget(QWidget):
    def __init__(self, theme, parent=None):
        super().__init__(parent)
        self.theme = theme
        self._offset = 0
        self._anim_timer = QTimer(self)
        self._anim_timer.timeout.connect(self._tick)
        self._anim_timer.start(40)

    def _tick(self):
        self._offset = (self._offset + 1) % 200
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        tc = TH[self.theme]
        w, h = self.width(), self.height()

        # Background gradient
        grad = QLinearGradient(0, 0, 0, h)
        grad.setColorAt(0, QColor(tc["bg"]))
        grad.setColorAt(1, QColor(tc["bg2"]))
        painter.fillRect(0, 0, w, h, grad)

        # Animated road lines
        painter.setOpacity(0.07)
        painter.setPen(QPen(QColor(tc["accent"]), 2))
        step = 40
        for x in range(-step, w + step, step):
            ox = (x + self._offset) % (w + step) - step // 2
            painter.drawLine(ox, 0, ox + w // 4, h)

        # Grid dots
        painter.setOpacity(0.04)
        painter.setBrush(QColor(tc["text"]))
        painter.setPen(Qt.PenStyle.NoPen)
        dot_step = 30
        for gx in range(0, w, dot_step):
            for gy in range(0, h, dot_step):
                painter.drawEllipse(gx, gy, 2, 2)

        painter.setOpacity(1.0)
        painter.end()


# ─────────────────────────── MAIN WINDOW ───────────────────────────
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.theme = "dark"
        self.lang = "en"
        self._sel_car = "red"
        self._sel_track = "city"
        self._sel_diff = "medium"

        self.setWindowTitle(TR[self.lang]["title"])
        self.setMinimumSize(700, 500)
        self.resize(1100, 700)

        self._central = QWidget()
        self.setCentralWidget(self._central)
        self._root_layout = QVBoxLayout(self._central)
        self._root_layout.setContentsMargins(0, 0, 0, 0)
        self._root_layout.setSpacing(0)

        self._bg = BackgroundWidget(self.theme, self._central)
        self._bg.setGeometry(self._central.rect())

        self._stack = QStackedWidget(self._central)
        self._stack.setStyleSheet("background:transparent;")
        self._root_layout.addWidget(self._stack)

        # Pages
        self._menu_pg = MenuPage(self.theme, self.lang)
        self._menu_pg.play_clicked.connect(self._go_select)
        self._menu_pg.settings_clicked.connect(self._go_settings)
        self._menu_pg.exit_clicked.connect(self.close)

        self._select_pg = CarSelectPage(self.theme, self.lang)
        self._select_pg.back_clicked.connect(self._go_menu)
        self._select_pg.start_clicked.connect(self._start_race)

        self._settings_pg = SettingsPage(self.theme, self.lang)
        self._settings_pg.back_clicked.connect(self._go_menu)
        self._settings_pg.theme_changed.connect(self._change_theme)
        self._settings_pg.lang_changed.connect(self._change_lang)

        self._game_pg = GamePage(self.theme, self.lang)
        self._game_pg.back_to_menu.connect(self._go_menu)
        self._game_pg.restart_requested.connect(self._restart_race)

        self._stack.addWidget(self._menu_pg)
        self._stack.addWidget(self._select_pg)
        self._stack.addWidget(self._settings_pg)
        self._stack.addWidget(self._game_pg)

        self._apply_theme()
        self._stack.setCurrentWidget(self._menu_pg)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._bg.setGeometry(self._central.rect())

    def _go_menu(self):
        self._game_pg.renderer.stop()
        self._stack.setCurrentWidget(self._menu_pg)

    def _go_select(self):
        self._stack.setCurrentWidget(self._select_pg)

    def _go_settings(self):
        self._stack.setCurrentWidget(self._settings_pg)

    def _start_race(self, car, track, diff):
        self._sel_car = car
        self._sel_track = track
        self._sel_diff = diff
        self._game_pg.theme = self.theme
        self._game_pg.lang = self.lang
        self._stack.setCurrentWidget(self._game_pg)
        self._game_pg.start_race(car, track, diff)

    def _restart_race(self):
        self._game_pg.start_race(self._sel_car, self._sel_track, self._sel_diff)

    def _change_theme(self, t):
        self.theme = t
        self._bg.theme = t
        self._apply_theme()
        self._menu_pg.theme = t
        self._menu_pg.refresh()
        self._select_pg.theme = t
        self._select_pg.refresh()
        self._settings_pg.theme = t
        self._settings_pg.refresh()
        self._game_pg.theme = t
        self._game_pg.refresh()

    def _change_lang(self, l):
        self.lang = l
        self.setWindowTitle(TR[l]["title"])
        self._menu_pg.lang = l
        self._menu_pg.refresh()
        self._select_pg.lang = l
        self._select_pg.refresh()
        self._settings_pg.lang = l
        self._settings_pg.refresh()
        self._game_pg.lang = l
        self._game_pg.refresh()

    def _apply_theme(self):
        tc = TH[self.theme]
        self.setStyleSheet(f"""
            QMainWindow {{
                background: {tc['bg']};
            }}
            QWidget {{
                font-family: 'Segoe UI', 'Arial', sans-serif;
            }}
            QScrollBar:vertical {{
                background: {tc['bg2']};
                width: 8px;
                border-radius: 4px;
            }}
            QScrollBar::handle:vertical {{
                background: {tc['accent']};
                border-radius: 4px;
            }}
        """)

    def closeEvent(self, event):
        tc = TH[self.theme]
        msg = QMessageBox(self)
        msg.setWindowTitle(TR[self.lang].get("exit", "Exit"))
        msg.setText(TR[self.lang]["exit"] + "?")
        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        msg.setDefaultButton(QMessageBox.StandardButton.No)
        msg.setStyleSheet(f"""
            QMessageBox {{
                background:{tc['card']};
                color:{tc['text']};
            }}
            QLabel {{
                color:{tc['text']};
                font-size:14px;
            }}
            QPushButton {{
                background:{tc['btn']};
                color:{tc['btn_text']};
                border:1.5px solid {tc['accent']};
                border-radius:8px;
                padding:7px 18px;
                font-size:13px;
                font-weight:bold;
                min-width:70px;
            }}
            QPushButton:hover {{
                background:{tc['btn_hover']};
                color:#ffffff;
            }}
        """)
        if msg.exec() == QMessageBox.StandardButton.Yes:
            self._game_pg.renderer.stop()
            event.accept()
        else:
            event.ignore()


# ─────────────────────────── ENTRY POINT ───────────────────────────
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Arcade Racing")
    app.setStyle("Fusion")

    try:
        app.setAttribute(Qt.ApplicationAttribute.AA_UseHighDpiPixmaps)
    except AttributeError:
        pass

    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
