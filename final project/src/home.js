import HeroSection from "./components/heroSection/heroSection";
import Navbar from "./components/navbar/navbar";

export default function Home() {
  return (
    <div>
      <Navbar />
      <main>
        <HeroSection />
      </main>
    </div>
  );
}
