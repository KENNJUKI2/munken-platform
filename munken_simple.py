
# Munken Platform - Sustainable Tourism & Clean Energy
print("🚀 Munken Platform Starting...")
print("🌍 Powering Sustainable Futures")

# Sample data
tours = [
    {"id": 1, "name": "Amazon Rainforest Conservation", "price": 120, "co2": 25.5},
    {"id": 2, "name": "Solar Farm Educational Tour", "price": 45, "co2": 12.0},
    {"id": 3, "name": "Coral Reef Restoration", "price": 85, "co2": 18.3}
]

solar_hubs = [
    {"name": "Sunshine Community Solar", "capacity": "500kW", "homes": 120}
]

bookings = []
total_co2_saved = 0.0

def main_menu():
    while True:
        print("\n" + "="*50)
        print("🌍 MUNKEN PLATFORM")
        print("="*50)
        print("1. View Eco Tours")
        print("2. View Solar Hubs")
        print("3. Book a Tour")
        print("4. My Impact")
        print("5. Platform Statistics")
        print("6. Exit")
        
        choice = input("\nChoose 1-6: ")
        
        if choice == "1":
            print("\n🏞️ ECO TOURS:")
            for tour in tours:
                print(f"{tour['id']}. {tour['name']}")
                print(f"   💰 ${tour['price']} | 🌱 {tour['co2']}kg CO2 saved")
        
        elif choice == "2":
            print("\n☀️ SOLAR HUBS:")
            for hub in solar_hubs:
                print(f"📍 {hub['name']}")
                print(f"   ⚡ {hub['capacity']} | 🏠 {hub['homes']} homes powered")
        
        elif choice == "3":
            print("\n📖 BOOK A TOUR:")
            for tour in tours:
                print(f"{tour['id']}. {tour['name']} - ${tour['price']}")
            
            try:
                tour_id = int(input("\nEnter tour ID: "))
                people = int(input("Number of participants: "))
                
                tour = next(t for t in tours if t['id'] == tour_id)
                co2_saved = tour['co2'] * people
                
                # Create booking
                booking = {
                    "tour": tour['name'],
                    "people": people,
                    "co2_saved": co2_saved,
                    "water_saved": people * 50
                }
                bookings.append(booking)
                
                # Update total impact
                global total_co2_saved
                total_co2_saved += co2_saved
                
                print(f"\n✅ BOOKING CONFIRMED!")
                print(f"📋 {tour['name']}")
                print(f"👥 {people} participants")
                print(f"🌱 {co2_saved}kg CO2 saved")
                print(f"💧 {people * 50} liters water saved")
                
            except:
                print("❌ Error - please check your inputs")
        
        elif choice == "4":
            print("\n📊 YOUR ENVIRONMENTAL IMPACT:")
            if not bookings:
                print("No bookings yet. Book a tour to make an impact! 🌍")
            else:
                total_water = sum(b['water_saved'] for b in bookings)
                print(f"Total Bookings: {len(bookings)}")
                print(f"Total CO2 Saved: {total_co2_saved}kg")
                print(f"Total Water Saved: {total_water} liters")
                print(f"🌳 Equivalent to planting {int(total_co2_saved / 20)} trees!")
        
        elif choice == "5":
            print("\n📈 PLATFORM STATISTICS:")
            print(f"Eco Tours: {len(tours)}")
            print(f"Solar Hubs: {len(solar_hubs)}")
            print(f"Total Bookings: {len(bookings)}")
            print(f"Total CO2 Reduced: {total_co2_saved}kg")
            print(f"Community Impact: ${len(bookings) * 50} contributed")
        
        elif choice == "6":
            print("\n💚 Thank you for using Munken Platform!")
            print("🌍 Together, we're building a sustainable future!")
            break
        
        else:
            print("❌ Please choose 1-6")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main_menu()
