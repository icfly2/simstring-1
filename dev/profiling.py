from pyinstrument import Profiler

profiler = Profiler() # or Profiler(use_signal=False), see below
profiler.start()

# code you want to profile

profiler.stop()

print(profiler.output_text(unicode=True, color=True))