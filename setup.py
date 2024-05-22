from distutils.core import setup
setup(
  name = 'mm_wlan',         
  packages = ['mm_wlan'],   
  version = '0.5',      
  license='MIT',       
  description = 'WLAN Connection functions in MicroPython',  
  author = 'Simon Monk and José Antonio Vacas',                  
  author_email = 'simon@monkmakes.com',      
  url = 'https://github.com/monkmakes/mm_wlan',  
  download_url = 'https://github.com/monkmakes/mm_wlan/archive/refs/tags/v_02.tar.gz',   
  keywords = ['WLAN', 'micropython', 'webserver'],  
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: Implementation :: MicroPython',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',     
  ],
)