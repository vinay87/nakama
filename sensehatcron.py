import datetime

from sense_hat import SenseHat

from nakama import get_latest_one_piece_chapter_jb, get_latest_one_piece_chapter_ms

if __name__ == "__main__":
    jaiminis_box = get_latest_one_piece_chapter_jb()
    s = SenseHat()
    s.set_rotation(180)
    if jaiminis_box["release_date"] == datetime.date.today():
        for i in range(10):
            s.show_message(
                "One Piece #{} {} out now on {}.".format(jaiminis_box["chapter_number"], jaiminis_box["chapter_name"], "Jaimini's Box"),
                    text_colour = [255,0,0],
                    scroll_speed = 0.2)
    else:
        mangastream = get_latest_one_piece_chapter_ms()
        if mangastream["release_date"] == datetime.date.today():
            for i in range(10):
                s.show_message(
                "One Piece #{} {} out now on {}.".format(mangastream["chapter_number"], mangastream["chapter_name"], "MangaStream"),
                text_colour = [255,0,0],
                scroll_speed = 0.2)
        else:
            s.show_message(
                "No new One Piece yet! :(.    Last chapter was: #{} {} @ {}.".format(mangastream["chapter_number"], mangastream["chapter_name"], "MangaStream"),
                text_colour = [0,255,0],
                scroll_speed = 0.2)

    s.set_rotation(0)
    s.clear()

