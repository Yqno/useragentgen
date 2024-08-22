from fake_useragent import UserAgent

# Create a UserAgent instance
ua = UserAgent()

# Ask the user if they want a specific or random User-Agent
choice = input("Would you like a specific User-Agent or a random one? (Enter 'specific' or 'random'): ").strip().lower()

if choice == 'specific':
    # Specific OS and browser options
    device_type = input("Do you want a mobile or desktop user-agent? (Enter 'mobile' or 'desktop'): ").strip().lower()

    if device_type == 'mobile':
        os_choice = input("Choose your mobile OS (ios, android): ").strip().lower()
        browser_choice = input("Choose your mobile browser (chrome, safari, firefox): ").strip().lower()

        if os_choice == 'ios':
            if browser_choice == 'safari':
                user_agent = ua.safari  # iOS Safari
            else:
                print("Invalid browser choice, defaulting to random iOS user-agent...")
                user_agent = ua.random
        elif os_choice == 'android':
            if browser_choice == 'chrome':
                user_agent = ua.chrome  # Android Chrome
            elif browser_choice == 'firefox':
                user_agent = ua.firefox  # Android Firefox
            else:
                print("Invalid browser choice, generating a random Android user-agent...")
                user_agent = ua.random
        else:
            print("Invalid OS, generating a random mobile user-agent...")
            user_agent = ua.random

    elif device_type == 'desktop':
        user_agent = ua.random  # For desktop, use random user-agent (more options)

    else:
        print("Invalid device type, generating a random user-agent...")
        user_agent = ua.random

elif choice == 'random':
    # Randomly generate the entire User-Agent
    user_agent = ua.random

else:
    # Handle invalid input by defaulting to a random User-Agent
    print("Invalid choice, generating a random User-Agent...")
    user_agent = ua.random

# Output the User-Agent string
print("Generated User-Agent:", user_agent)

