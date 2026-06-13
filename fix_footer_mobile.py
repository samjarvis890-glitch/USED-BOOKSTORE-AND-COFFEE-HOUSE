import os
import glob

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Logo & Description parent is already text-center md:text-left? Let's check it.
    # We will modify Logo & Description to text-center md:text-left
    if '<!-- Logo & Description -->\n        <div class="space-y-6">' in content:
        content = content.replace(
            '<!-- Logo & Description -->\n        <div class="space-y-6">',
            '<!-- Logo & Description -->\n        <div class="space-y-6 text-center md:text-left">'
        )
    # the logo image parent:
    if '<div class="bg-[#F8F5F0] p-3 rounded-2xl inline-block shadow-lg border-2 border-[#C4A484]/50 transition-transform duration-300 hover:-translate-y-1">' in content:
        content = content.replace(
            '<div class="bg-[#F8F5F0] p-3 rounded-2xl inline-block shadow-lg border-2 border-[#C4A484]/50 transition-transform duration-300 hover:-translate-y-1">',
            '<div class="bg-[#F8F5F0] p-3 rounded-2xl inline-block shadow-lg border-2 border-[#C4A484]/50 transition-transform duration-300 hover:-translate-y-1 mx-auto md:mx-0">'
        )
    # the social icons parent
    if '<div class="flex gap-4">' in content:
        content = content.replace(
            '<div class="flex gap-4">',
            '<div class="flex gap-4 justify-center md:justify-start">'
        )

    # "Explore" section div
    content = content.replace(
        '<!-- Explore -->\n        <div>',
        '<!-- Explore -->\n        <div class="text-center md:text-left">'
    )
    # the underline in Explore:
    content = content.replace(
        '''Explore\n            <span class="absolute -bottom-2 left-0 w-1/2 h-0.5 bg-[#C4A484]"></span>''',
        '''Explore\n            <span class="absolute -bottom-2 left-1/2 -translate-x-1/2 md:left-0 md:translate-x-0 w-1/2 h-0.5 bg-[#C4A484]"></span>'''
    )
    # The UL in Explore
    content = content.replace(
        '<ul class="space-y-3 text-sm">',
        '<ul class="space-y-3 text-sm flex flex-col items-center md:items-start">'
    )
    
    # "Visit Us" section div
    content = content.replace(
        '<!-- Visit Us -->\n        <div>',
        '<!-- Visit Us -->\n        <div class="text-center md:text-left">'
    )
    # the underline in Visit Us:
    content = content.replace(
        '''Visit Us\n            <span class="absolute -bottom-2 left-0 w-1/2 h-0.5 bg-[#C4A484]"></span>''',
        '''Visit Us\n            <span class="absolute -bottom-2 left-1/2 -translate-x-1/2 md:left-0 md:translate-x-0 w-1/2 h-0.5 bg-[#C4A484]"></span>'''
    )
    # The UL in Visit Us
    content = content.replace(
        '<ul class="space-y-4 text-sm text-[#c4b3a0]">',
        '<ul class="space-y-4 text-sm text-[#c4b3a0] flex flex-col items-center md:items-start">'
    )
    # For Visit us LIs to be text-center md:text-left
    # <li class="flex items-start gap-3">
    content = content.replace(
        '<li class="flex items-start gap-3">',
        '<li class="flex flex-col md:flex-row items-center md:items-start gap-3 text-center md:text-left">'
    )
    # Also change the mt-1 on the icons to mb-2 md:mb-0 md:mt-1
    content = content.replace(
        '<i class="fas fa-map-marker-alt text-[#C4A484] mt-1 text-lg"></i>',
        '<i class="fas fa-map-marker-alt text-[#C4A484] mb-2 md:mb-0 md:mt-1 text-lg"></i>'
    )
    content = content.replace(
        '<i class="fas fa-clock text-[#C4A484] mt-1 text-lg"></i>',
        '<i class="fas fa-clock text-[#C4A484] mb-2 md:mb-0 md:mt-1 text-lg"></i>'
    )
    content = content.replace(
        '<i class="fas fa-envelope text-[#C4A484] mt-1 text-lg"></i>',
        '<i class="fas fa-envelope text-[#C4A484] mb-2 md:mb-0 md:mt-1 text-lg"></i>'
    )
    
    # "Join the Club" / Newsletter section div
    content = content.replace(
        '<!-- Newsletter -->\n        <div>',
        '<!-- Newsletter -->\n        <div class="text-center md:text-left">'
    )
    # the underline in Join the Club:
    content = content.replace(
        '''Join the Club\n            <span class="absolute -bottom-2 left-0 w-1/2 h-0.5 bg-[#C4A484]"></span>''',
        '''Join the Club\n            <span class="absolute -bottom-2 left-1/2 -translate-x-1/2 md:left-0 md:translate-x-0 w-1/2 h-0.5 bg-[#C4A484]"></span>'''
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
