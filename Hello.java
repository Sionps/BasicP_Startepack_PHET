class Dog {
    String name;
    String breed;
    int age;

    void bark() {
        System.out.println(name + "Woof!" + getAge());
    }

    void fetch(String item) {
        System.out.println(name + "is fetching the " + item);
    }
    
    String getAge() {
        return "My dog's age is " + age;
    }
    
}

class Hello {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.name = "Buddy";
        myDog.age = 3;
        myDog.breed = "Golden Retriever";

        myDog.bark();
        myDog.fetch("ball");
    }
}