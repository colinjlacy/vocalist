from unittest import TestCase
from unittest import mock
from main import Listener
import os
import speech_recognition as sr
from io import StringIO

class ListenerTest(TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_successful_strategy_mapping(self):
        try:
            _ = Listener(strategy="sphinx")
            assert True
        except KeyError:
            self.fail()
        except Exception:
            self.fail()

    def test_erroneous_strategy_mapping(self):
        try:
            _ = Listener(strategy="testException")
            self.fail()
        except KeyError:
            self.assertRaises(KeyError)
        except Exception:
            self.fail()

    def test_pyaudio_not_installed(self):
        with mock.patch('speech_recognition.Microphone') as mocked_mic:
            mocked_mic.side_effect = AttributeError("test")
            try:
                _ = Listener()
                self.fail()
            except AttributeError as err:
                self.assertEqual("You'll need to install PyAudio first: https://people.csail.mit.edu/hubert/pyaudio/", str(err))
            except Exception:
                self.fail()

    def test_no_mic_found(self):
        with mock.patch('speech_recognition.Microphone', return_value=None):
            l = Listener()
            try:
                l.listen()
                self.fail()
            except NameError as err:
                self.assertEqual("Could not find a suitable microphone.", str(err))
            except Exception:
                self.fail()

    def test_could_not_parse_text(self):
        harvard = sr.AudioFile('harvard.wav')
        os.system = mock.MagicMock()
        l = Listener()
        with harvard as source:
            audio = l.recognizer.record(source)
        l.recognizer.recognize_google = mock.MagicMock(return_value=audio)
        l.recognizer.listen = mock.MagicMock()
        l.recognizer.recognize_google.side_effect = sr.UnknownValueError("test")
        with mock.patch('speech_recognition.Microphone.listen') as mocked_mic:
            l.listen()
        # with mock.patch('speech_recognition.Recognizer.recognize_sphinx', return_value=None, new_callable=None) as mocked_recognizer:
        #     mocked_recognizer.side_effect = sr.UnknownValueError("test")
            assert os.system.called
