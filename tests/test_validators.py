# -*- coding: utf-8 -*-

from python_usernames import is_safe_username


def test_max_lenght():
    assert is_safe_username("u" * 10, max_length=10)
    assert not is_safe_username("u" * 11, max_length=10)


def test_blacklist():
    assert not is_safe_username("helo", blacklist=["helo"])
    assert not is_safe_username("helo", blacklist=["Helo"])


def test_whitelist():
    assert not is_safe_username("he..lo", whitelist=["he..lo"])
    assert is_safe_username("fuck", whitelist=["fuck"])
    assert is_safe_username("fuck", whitelist=["Fuck"])


def test_usernames():
    unsafe_words = [
        "!",
        "#",
        "",
        "()",
        "-",
        "-hello",
        ".",
        ".hello",
        "_",
        "a@!/",
        "fuck",
        "hel--lo",
        "hel-.lo",
        "hel..lo",
        "hel__lo",
        "hello-",
        "hello.",
        "sex",
        "\\",
        "\\\\",
        "--1",
        "!@#$%^&*()`~",
        "`⁄€‹›ﬁﬂ‡°·‚—±",
        "⅛⅜⅝⅞",
        "😍",
        "👩🏽",
        "👾 🙇 💁 🙅 🙆 🙋 🙎 🙍 ",
        "🐵 🙈 🙉 🙊",
        "❤️ 💔 💌 💕 💞 💓 💗 💖 💘 💝 💟 💜 💛 💚 💙",
        "✋🏿 💪🏿 👐🏿 🙌🏿 👏🏿 🙏🏿",
        "🚾 🆒 🆓 🆕 🆖 🆗 🆙 🏧",
        "0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 🔟",
        "１２３",
        "١٢٣",
        "ثم نفس سقطت وبالتحديد،, جزيرتي باستخدام أن دنو. إذ هنا؟ الستار وتنصيب كان. أهّل ايطاليا، بريطانيا-فرنسا قد أخذ. سليمان، إتفاقية بين ما, يذكر الحدود أي بعد, معاملة بولندا، الإطلاق عل إيو.",  # noqa
        "בְּרֵאשִׁית, בָּרָא אֱלֹהִים, אֵת הַשָּׁמַיִם, וְאֵת הָאָרֶץ",
        "הָיְתָהtestالصفحات التّحول",
        "﷽",
        "ﷺ",
        " ",
        "𝐓𝐡𝐞",
        "⒯⒣⒠",
        "Powerلُلُصّبُلُلصّبُررًॣॣhॣॣ冗",
    ]

    safe_words = [
        "a" "10101",
        "1he-llo",
        "_hello",
        "he-llo",
        "he.llo_",
        "hello",
        "hello_",
        "999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
    ]

    for w in unsafe_words:
        assert not is_safe_username(w)

    for w in safe_words:
        assert is_safe_username(w)
